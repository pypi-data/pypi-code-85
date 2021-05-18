# copyright 2003-2016 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of CubicWeb.
#
# CubicWeb is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# CubicWeb is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with CubicWeb.  If not, see <http://www.gnu.org/licenses/>.
"""Helper classes to execute RQL queries on a set of sources, performing
security checking and data aggregation.
"""
import uuid
import time
import traceback
from itertools import repeat
from threading import Lock

from cachetools import LFUCache

from rql import RQLSyntaxError, CoercionError
from rql.stmts import Union
from rql.nodes import ETYPE_PYOBJ_MAP, etype_from_pyobj, Relation, Exists, Not,\
    VariableRef, Constant
from yams import BASE_TYPES

from cubicweb import ValidationError, Unauthorized, UnknownEid, QueryError
from cubicweb.rqlrewrite import RQLRelationRewriter
from cubicweb import Binary, server
from cubicweb.rset import ResultSet
from cubicweb.debug import emit_to_debug_channel

from cubicweb.utils import RepeatList
from cubicweb.misc.source_highlight import highlight_terminal
from cubicweb.server.rqlannotation import RQLAnnotator, set_qdata
from cubicweb.server.ssplanner import (READ_ONLY_RTYPES, add_types_restriction,
                                       prepare_plan)
from cubicweb.server.edition import EditedEntity

ETYPE_PYOBJ_MAP[Binary] = 'Bytes'


def empty_rset(rql, args):
    """build an empty result set object"""
    return ResultSet([], rql, args)


# permission utilities ########################################################

def check_no_password_selected(rqlst):
    """check that Password entities are not selected"""
    for solution in rqlst.solutions:
        for var, etype in solution.items():
            if etype == 'Password':
                raise Unauthorized('Password selection is not allowed (%s)' % var)

def term_etype(cnx, term, solution, args):
    """return the entity type for the given term (a VariableRef or a Constant
    node)
    """
    try:
        return solution[term.name]
    except AttributeError:
        return cnx.entity_type(term.eval(args))

def check_relations_read_access(cnx, select, args):
    """Raise :exc:`Unauthorized` if the given user doesn't have credentials to
    read relations used in the given syntax tree
    """
    # use `term_etype` since we've to deal with rewritten constants here,
    # when used as an external source by another repository.
    # XXX what about local read security w/ those rewritten constants...
    # XXX constants can also happen in some queries generated by req.find()
    DBG = (server.DEBUG & server.DBG_SEC) and 'read' in server._SECURITY_CAPS
    schema = cnx.repo.schema
    user = cnx.user
    if select.where is not None:
        for rel in select.where.iget_nodes(Relation):
            for solution in select.solutions:
                # XXX has_text may have specific perm ?
                if rel.r_type in READ_ONLY_RTYPES:
                    continue
                rschema = schema.rschema(rel.r_type)
                if rschema.final:
                    eschema = schema.eschema(term_etype(cnx, rel.children[0],
                                             solution, args))
                    rdef = eschema.rdef(rschema)
                else:
                    rdef = rschema.rdef(term_etype(cnx, rel.children[0],
                                                   solution, args),
                                        term_etype(cnx, rel.children[1].children[0],
                                                   solution, args))
                if not user.matching_groups(rdef.get_groups('read')):
                    if DBG:
                        print('check_read_access: %s %s does not match %s' %
                              (rdef, user.groups, rdef.get_groups('read')))
                    # XXX rqlexpr not allowed
                    raise Unauthorized('read', rel.r_type)
                if DBG:
                    print('check_read_access: %s %s matches %s' %
                          (rdef, user.groups, rdef.get_groups('read')))

def get_local_checks(cnx, rqlst, solution):
    """Check that the given user has credentials to access data read by the
    query and return a dict defining necessary "local checks" (i.e. rql
    expression in read permission defined in the schema) where no group grants
    him the permission.

    Returned dictionary's keys are variable names and values the rql expressions
    for this variable (with the given solution).

    Raise :exc:`Unauthorized` if access is known to be defined, i.e. if there is
    no matching group and no local permissions.
    """
    DBG = (server.DEBUG & server.DBG_SEC) and 'read' in server._SECURITY_CAPS
    schema = cnx.repo.schema
    user = cnx.user
    localchecks = {}
    # iterate on defined_vars and not on solutions to ignore column aliases
    for varname in rqlst.defined_vars:
        eschema = schema.eschema(solution[varname])
        if eschema.final:
            continue
        if not user.matching_groups(eschema.get_groups('read')):
            erqlexprs = eschema.get_rqlexprs('read')
            if not erqlexprs:
                ex = Unauthorized('read', solution[varname])
                ex.var = varname
                if DBG:
                    print('check_read_access: %s %s %s %s' %
                          (varname, eschema, user.groups, eschema.get_groups('read')))
                raise ex
            # don't insert security on variable only referenced by 'NOT X relation Y' or
            # 'NOT EXISTS(X relation Y)'
            varinfo = rqlst.defined_vars[varname].stinfo
            if varinfo['selected'] or (
                len([r for r in varinfo['relations']
                     if (not schema.rschema(r.r_type).final
                         and ((isinstance(r.parent, Exists) and r.parent.neged(strict=True))
                              or isinstance(r.parent, Not)))])
                !=
                len(varinfo['relations'])):
                localchecks[varname] = erqlexprs
    return localchecks


# Plans #######################################################################

class ExecutionPlan(object):
    """the execution model of a rql query, composed of querier steps"""

    def __init__(self, schema, rqlst, args, cnx):
        self.schema = schema
        # original rql syntax tree
        self.rqlst = rqlst
        self.args = args or {}
        # cnx executing the query
        self.cnx = cnx
        # execution steps
        self.steps = []
        # tracing token for debugging
        self.rql_query_tracing_token = None

    def add_step(self, step):
        """add a step to the plan"""
        self.steps.append(step)

    def sqlexec(self, sql, args=None):
        return self.cnx.repo.system_source.sqlexec(self.cnx, sql, args)

    def execute(self):
        """execute a plan and return resulting rows"""
        for step in self.steps:
            step.rql_query_tracing_token = self.rql_query_tracing_token
            result = step.execute()
        # the latest executed step contains the full query result
        return result

    def preprocess(self, union, security=True):
        """insert security when necessary then annotate rql syntax tree
        to prepare sql generation
        """
        cached = None
        if security and self.cnx.read_security:
            # ensure security is turned off when security is inserted,
            # else we may loop for ever...
            if self.cnx.transaction_data.get('security-rqlst-cache'):
                key = self.cache_key
            else:
                key = None
            if key is not None and key in self.cnx.transaction_data:
                cachedunion, args = self.cnx.transaction_data[key]
                union.children[:] = []
                for select in cachedunion.children:
                    union.append(select)
                union.has_text_query = cachedunion.has_text_query
                args.update(self.args)
                self.args = args
                cached = True
            else:
                with self.cnx.security_enabled(read=False):
                    noinvariant = self._insert_security(union)
                if key is not None:
                    self.cnx.transaction_data[key] = (union, self.args)
        else:
            noinvariant = ()
        if cached is None:
            self.cnx.vreg.rqlhelper.simplify(union)
            RQLAnnotator(self.schema).annotate(union)
            set_qdata(self.schema.rschema, union, noinvariant)
        if union.has_text_query:
            self.cache_key = None

    def _insert_security(self, union):
        noinvariant = set()
        for select in union.children[:]:
            for subquery in select.with_:
                self._insert_security(subquery.query)
            localchecks, restricted = self._check_permissions(select)
            if any(localchecks):
                self.cnx.rql_rewriter.insert_local_checks(
                    select, self.args, localchecks, restricted, noinvariant)
        return noinvariant

    def _check_permissions(self, rqlst):
        """Return a dict defining "local checks", i.e. RQLExpression defined in
        the schema that should be inserted in the original query, together with
        a set of variable names which requires some security to be inserted.

        Solutions where a variable has a type which the user can't definitly
        read are removed, else if the user *may* read it (i.e. if an rql
        expression is defined for the "read" permission of the related type),
        the local checks dict is updated.

        The local checks dict has entries for each different local check
        necessary, with associated solutions as value, a local check being
        defined by a list of 2-uple (variable name, rql expressions) for each
        variable which has to be checked. Solutions which don't require local
        checks will be associated to the empty tuple key.

        Note rqlst should not have been simplified at this point.
        """
        cnx = self.cnx
        msgs = []
        # dict(varname: eid), allowing to check rql expression for variables
        # which have a known eid
        varkwargs = {}
        if not cnx.transaction_data.get('security-rqlst-cache'):
            for var in rqlst.defined_vars.values():
                if var.stinfo['constnode'] is not None:
                    eid = var.stinfo['constnode'].eval(self.args)
                    varkwargs[var.name] = int(eid)
        # dictionary of variables restricted for security reason
        localchecks = {}
        restricted_vars = set()
        newsolutions = []
        for solution in rqlst.solutions:
            try:
                localcheck = get_local_checks(cnx, rqlst, solution)
            except Unauthorized as ex:
                msg = 'remove %s from solutions since %s has no %s access to %s'
                msg %= (solution, cnx.user.login, ex.args[0], ex.args[1])
                msgs.append(msg)
                LOGGER.info(msg)
            else:
                newsolutions.append(solution)
                # try to benefit of rqlexpr.check cache for entities which
                # are specified by eid in query'args
                for varname, eid in varkwargs.items():
                    try:
                        rqlexprs = localcheck.pop(varname)
                    except KeyError:
                        continue
                    # if entity has been added in the current transaction, the
                    # user can read it whatever rql expressions are associated
                    # to its type
                    if cnx.added_in_transaction(eid):
                        continue
                    for rqlexpr in rqlexprs:
                        if rqlexpr.check(cnx, eid):
                            break
                    else:
                        raise Unauthorized('No read access on %r with eid %i.' % (var, eid))
                # mark variables protected by an rql expression
                restricted_vars.update(localcheck)
                # turn local check into a dict key
                localcheck = tuple(sorted(localcheck.items()))
                localchecks.setdefault(localcheck, []).append(solution)
        # raise Unautorized exception if the user can't access to any solution
        if not newsolutions:
            raise Unauthorized('\n'.join(msgs))
        # if there is some message, solutions have been modified and must be
        # reconsidered by the syntax treee
        if msgs:
            rqlst.set_possible_types(newsolutions)
        return localchecks, restricted_vars

    def finalize(self, select, solutions, insertedvars):
        rqlst = Union()
        rqlst.append(select)
        for mainvarname, rschema, newvarname in insertedvars:
            nvartype = str(rschema.objects(solutions[0][mainvarname])[0])
            for sol in solutions:
                sol[newvarname] = nvartype
        select.clean_solutions(solutions)
        add_types_restriction(self.schema, select)
        self.cnx.vreg.rqlhelper.annotate(rqlst)
        self.preprocess(rqlst, security=False)
        return rqlst


class InsertPlan(ExecutionPlan):
    """an execution model specific to the INSERT rql query
    """

    def __init__(self, schema, rqlst, args, cnx):
        ExecutionPlan.__init__(self, schema, rqlst, args, cnx)
        # save originally selected variable, we may modify this
        # dictionary for substitution (query parameters)
        self.selected = rqlst.selection
        # list of rows of entities definition (ssplanner.EditedEntity)
        self.e_defs = [[]]
        # list of new relation definition (3-uple (from_eid, r_type, to_eid)
        self.r_defs = set()
        # indexes to track entity definitions bound to relation definitions
        self._r_subj_index = {}
        self._r_obj_index = {}
        self._expanded_r_defs = {}

    def add_entity_def(self, edef):
        """add an entity definition to build"""
        self.e_defs[-1].append(edef)

    def add_relation_def(self, rdef):
        """add an relation definition to build"""
        edef, rtype, value = rdef
        if self.schema[rtype].rule:
            raise QueryError("'%s' is a computed relation" % rtype)
        self.r_defs.add(rdef)
        if not isinstance(edef, int):
            self._r_subj_index.setdefault(edef, []).append(rdef)
        if not isinstance(value, int):
            self._r_obj_index.setdefault(value, []).append(rdef)

    def substitute_entity_def(self, edef, edefs):
        """substitute an incomplete entity definition by a list of complete
        equivalents

        e.g. on queries such as ::
          INSERT Personne X, Societe Y: X nom N, Y nom 'toto', X travaille Y
          WHERE U login 'admin', U login N

        X will be inserted as many times as U exists, and so the X travaille Y
        relations as to be added as many time as X is inserted
        """
        if not edefs or not self.e_defs:
            # no result, no entity will be created
            self.e_defs = ()
            return
        # first remove the incomplete entity definition
        colidx = self.e_defs[0].index(edef)
        for i, row in enumerate(self.e_defs[:]):
            self.e_defs[i][colidx] = edefs[0]
            samplerow = self.e_defs[i]
            for edef_ in edefs[1:]:
                row = [ed.clone() for i, ed in enumerate(samplerow)
                       if i != colidx]
                row.insert(colidx, edef_)
                self.e_defs.append(row)
        # now, see if this entity def is referenced as subject in some relation
        # definition
        if edef in self._r_subj_index:
            for rdef in self._r_subj_index[edef]:
                expanded = self._expanded(rdef)
                result = []
                for exp_rdef in expanded:
                    for edef_ in edefs:
                        result.append( (edef_, exp_rdef[1], exp_rdef[2]) )
                self._expanded_r_defs[rdef] = result
        # and finally, see if this entity def is referenced as object in some
        # relation definition
        if edef in self._r_obj_index:
            for rdef in self._r_obj_index[edef]:
                expanded = self._expanded(rdef)
                result = []
                for exp_rdef in expanded:
                    for edef_ in edefs:
                        result.append( (exp_rdef[0], exp_rdef[1], edef_) )
                self._expanded_r_defs[rdef] = result

    def _expanded(self, rdef):
        """return expanded value for the given relation definition"""
        try:
            return self._expanded_r_defs[rdef]
        except KeyError:
            self.r_defs.remove(rdef)
            return [rdef]

    def relation_defs(self):
        """return the list for relation definitions to insert"""
        for rdefs in self._expanded_r_defs.values():
            for rdef in rdefs:
                yield rdef
        for rdef in self.r_defs:
            yield rdef

    def insert_entity_defs(self):
        """return eids of inserted entities in a suitable form for the resulting
        result set, e.g.:

        e.g. on queries such as ::
          INSERT Personne X, Societe Y: X nom N, Y nom 'toto', X travaille Y
          WHERE U login 'admin', U login N

        if there is two entities matching U, the result set will look like
        [(eidX1, eidY1), (eidX2, eidY2)]
        """
        cnx = self.cnx
        repo = cnx.repo
        results = []
        for row in self.e_defs:
            results.append([repo.glob_add_entity(cnx, edef)
                            for edef in row])
        return results

    def insert_relation_defs(self):
        cnx = self.cnx
        repo = cnx.repo
        edited_entities = {}
        relations = {}
        for subj, rtype, obj in self.relation_defs():
            # if a string is given into args instead of an int, we get it here
            if isinstance(subj, str):
                subj = int(subj)
            elif not isinstance(subj, int):
                subj = subj.entity.eid
            if isinstance(obj, str):
                obj = int(obj)
            elif not isinstance(obj, int):
                obj = obj.entity.eid
            if repo.schema.rschema(rtype).inlined:
                if subj not in edited_entities:
                    entity = cnx.entity_from_eid(subj)
                    edited = EditedEntity(entity)
                    edited_entities[subj] = edited
                else:
                    edited = edited_entities[subj]
                edited.edited_attribute(rtype, obj)
            else:
                if rtype in relations:
                    relations[rtype].append((subj, obj))
                else:
                    relations[rtype] = [(subj, obj)]
        repo.glob_add_relations(cnx, relations)
        for edited in edited_entities.values():
            repo.glob_update_entity(cnx, edited)


class QuerierHelper(object):
    """helper class to execute rql queries, putting all things together"""

    def __init__(self, repo, schema):
        # system info helper
        self._repo = repo
        # instance schema
        self.set_schema(schema)

    def set_schema(self, schema):
        self.schema = schema
        self.clear_caches()

    def clear_caches(self, eids=None, etypes=None):
        if eids is None:
            self.rql_cache = RQLCache(self._repo, self.schema)
        else:
            cache = self.rql_cache
            for eid, etype in zip(eids, etypes):
                cache.pop(('Any X WHERE X eid %s' % eid,), None)
                if etype is not None:
                    cache.pop(('%s X WHERE X eid %s' % (etype, eid),), None)

    def plan_factory(self, rqlst, args, cnx):
        """create an execution plan for an INSERT RQL query"""
        if rqlst.TYPE == 'insert':
            return InsertPlan(self.schema, rqlst, args, cnx)
        return ExecutionPlan(self.schema, rqlst, args, cnx)

    def execute(self, cnx, rql, args=None, build_descr=True):
        """execute a rql query, return resulting rows and their description in
        a `ResultSet` object

        * `rql` should be a Unicode string or a plain ASCII string
        * `args` the optional parameters dictionary associated to the query
        * `build_descr` is a boolean flag indicating if the description should
          be built on select queries (if false, the description will be en empty
          list)

        on INSERT queries, there will be one row with the eid of each inserted
        entity

        result for DELETE and SET queries is undefined yet

        to maximize the rql parsing/analyzing cache performance, you should
        always use substitute arguments in queries (i.e. avoid query such as
        'Any X WHERE X eid 123'!)
        """
        if server.DEBUG & (server.DBG_RQL | server.DBG_SQL):
            if server.DEBUG & (server.DBG_MORE | server.DBG_SQL):
                print('*'*80)
            print("querier input", highlight_terminal(repr(rql)[1:-1], 'RQL'), repr(args))
        try:
            rqlst, cachekey = self.rql_cache.get(cnx, rql, args)
        except UnknownEid:
            # we want queries such as "Any X WHERE X eid 9999"
            # return an empty result instead of raising UnknownEid
            return empty_rset(rql, args)
        if rqlst.TYPE != 'select':
            if cnx.read_security:
                check_no_password_selected(rqlst)
            cachekey = None
        else:
            if cnx.read_security:
                for select in rqlst.children:
                    check_no_password_selected(select)
                    check_relations_read_access(cnx, select, args)
            # on select query, always copy the cached rqlst so we don't have to
            # bother modifying it. This is not necessary on write queries since
            # a new syntax tree is built from them.
            rqlst = rqlst.copy()
            # Rewrite computed relations
            rewriter = RQLRelationRewriter(cnx)
            rewriter.rewrite(rqlst, args)
            self._repo.vreg.rqlhelper.annotate(rqlst)
            if args:
                # different SQL generated when some argument is None or not (IS
                # NULL). This should be considered when computing sql cache key
                cachekey += tuple(sorted([k for k, v in args.items()
                                          if v is None]))
        # make an execution plan
        plan = self.plan_factory(rqlst, args, cnx)
        plan.cache_key = cachekey
        plan.rql_query_tracing_token = str(uuid.uuid4())
        prepare_plan(plan, self.schema, self._repo.vreg.rqlhelper)

        query_debug_informations = {
            "rql": rql,
            "rql_query_tracing_token": plan.rql_query_tracing_token,
            "args": args,
            # remove the last part of the stack which is: this line
            "callstack": "".join(traceback.format_stack()[:-1]),
            "description": "",
        }

        start = time.time()
        # execute the plan
        try:
            results = plan.execute()
        except (Unauthorized, ValidationError):
            # getting an Unauthorized/ValidationError exception means the
            # transaction must be rolled back
            #
            # notes:
            # * we should not reset the connections set here, since we don't want the
            #   connection to loose it during processing
            # * don't rollback if we're in the commit process, will be handled
            #   by the connection
            if cnx.commit_state is None:
                cnx.commit_state = 'uncommitable'
            raise

        query_debug_informations["time"] = ((time.time() - start) * 1000)
        query_debug_informations["result"] = results

        # build a description for the results if necessary
        descr = ()
        variables = None
        if build_descr:
            if rqlst.TYPE == 'select':
                # sample selection
                if len(rqlst.children) == 1 and len(rqlst.children[0].solutions) == 1:
                    # easy, all lines are identical
                    selected = rqlst.children[0].selection
                    solution = rqlst.children[0].solutions[0]
                    description = _make_description(selected, args, solution)
                    descr = RepeatList(len(results), tuple(description))
                    variables = [self._get_projected_name(projected, rqlst.children[0].stinfo)
                                 for projected in selected]
                else:
                    # hard, delegate the work :o)
                    descr = manual_build_descr(cnx, rqlst, args, results)
            elif rqlst.TYPE == 'insert':
                # on insert plan, some entities may have been auto-casted,
                # so compute description manually even if there is only
                # one solution
                basedescr = [None] * len(plan.selected)
                todetermine = list(zip(range(len(plan.selected)), repeat(False)))
                descr = _build_descr(cnx, results, basedescr, todetermine)
            # FIXME: get number of affected entities / relations on non
            # selection queries ?
            query_debug_informations["description"] = descr

        emit_to_debug_channel("rql", query_debug_informations)

        # return a result set object
        return ResultSet(results, rql, args, descr, variables)

    # these are overridden by set_log_methods below
    # only defining here to prevent pylint from complaining
    info = warning = error = critical = exception = debug = lambda msg,*a,**kw: None

    @staticmethod
    def _get_projected_name(projected, stinfo):
        if isinstance(projected, VariableRef):
            return projected.name
        elif isinstance(projected, Constant):
            if stinfo['rewritten'] is None:
                return str(projected)
            for name, value in stinfo['rewritten'].items():
                if [projected] == value:
                    return name
        return str(projected)


class RQLCache(object):

    def __init__(self, repo, schema):
        # rql st and solution cache.
        self._cache = LFUCache(repo.config['rql-cache-size'])
        self._lock = Lock()
        # rql cache key cache. Don't bother using a Cache instance: we should
        # have a limited number of queries in there, since there are no entries
        # in this cache for user queries (which have no args)
        self._ck_cache = {}
        # some cache usage stats
        self.cache_hit, self.cache_miss = 0, 0
        # rql parsing / analysing helper
        self.compute_var_types = repo.vreg.compute_var_types
        rqlhelper = repo.vreg.rqlhelper
        # set backend on the rql helper, will be used for function checking
        rqlhelper.backend = repo.config.system_source_config['db-driver']

        def parse(rql, annotate=False, parse=rqlhelper.parse):
            """Return a freshly parsed syntax tree for the given RQL."""
            try:
                return parse(rql, annotate=annotate)
            except UnicodeError:
                raise RQLSyntaxError(rql)
        self._parse = parse

    def __len__(self):
        with self._lock:
            return len(self._cache)

    def get(self, cnx, rql, args):
        """Return syntax tree and cache key for the given RQL.

        Returned syntax tree is cached and must not be modified
        """
        with self._lock:
            # parse the query and binds variables
            cachekey = (rql,)
            try:
                if args:
                    # search for named args in query which are eids (hence
                    # influencing query's solutions)
                    eidkeys = self._ck_cache[rql]
                    if eidkeys:
                        # if there are some, we need a better cache key, eg (rql +
                        # entity type of each eid)
                        cachekey = _rql_cache_key(cnx, rql, args, eidkeys)
                rqlst = self._cache[cachekey]
                self.cache_hit += 1
            except KeyError:
                self.cache_miss += 1
                rqlst = self._parse(rql)
                # compute solutions for rqlst and return named args in query
                # which are eids. Notice that if you may not need `eidkeys`, we
                # have to compute solutions anyway (kept as annotation on the
                # tree)
                eidkeys = self.compute_var_types(cnx, rqlst, args)
                if args and rql not in self._ck_cache:
                    self._ck_cache[rql] = eidkeys
                    if eidkeys:
                        cachekey = _rql_cache_key(cnx, rql, args, eidkeys)
                self._cache[cachekey] = rqlst
            return rqlst, cachekey

    def pop(self, key, *args):
        """Pop a key from the cache."""
        with self._lock:
            self._cache.pop(key, *args)


def _rql_cache_key(cnx, rql, args, eidkeys):
    cachekey = [rql]
    type_from_eid = cnx.repo.type_from_eid
    for key in sorted(eidkeys):
        try:
            etype = type_from_eid(args[key], cnx)
        except KeyError:
            raise QueryError('bad cache key %s (no value)' % key)
        except TypeError:
            raise QueryError('bad cache key %s (value: %r)' % (
                key, args[key]))
        cachekey.append(etype)
        # ensure eid is correctly typed in args
        args[key] = int(args[key])
    return tuple(cachekey)


from logging import getLogger
from cubicweb import set_log_methods
LOGGER = getLogger('cubicweb.querier')
set_log_methods(QuerierHelper, LOGGER)


def manual_build_descr(cnx, rqlst, args, result):
    """build a description for a given result by analysing each row

    XXX could probably be done more efficiently during execution of query
    """
    # not so easy, looks for variable which changes from one solution
    # to another
    unstables = rqlst.get_variable_indices()
    basedescr = []
    todetermine = []
    for i in range(len(rqlst.children[0].selection)):
        ttype = _selection_idx_type(i, rqlst, args)
        if ttype is None or ttype == 'Any':
            ttype = None
            isfinal = True
        else:
            isfinal = ttype in BASE_TYPES
        if ttype is None or i in unstables:
            basedescr.append(None)
            todetermine.append( (i, isfinal) )
        else:
            basedescr.append(ttype)
    if not todetermine:
        return RepeatList(len(result), tuple(basedescr))
    return _build_descr(cnx, result, basedescr, todetermine)

def _build_descr(cnx, result, basedescription, todetermine):
    description = []
    entity_type = cnx.entity_type
    todel = []
    for i, row in enumerate(result):
        row_descr = basedescription[:]
        for index, isfinal in todetermine:
            value = row[index]
            if value is None:
                # None value inserted by an outer join, no type
                row_descr[index] = None
                continue
            if isfinal:
                row_descr[index] = etype_from_pyobj(value)
            else:
                try:
                    row_descr[index] = entity_type(value)
                except UnknownEid:
                    cnx.error('wrong eid %s in repository, you should '
                             'db-check the database' % value)
                    todel.append(i)
                    break
        else:
            description.append(tuple(row_descr))
    for i in reversed(todel):
        del result[i]
    return description

def _make_description(selected, args, solution):
    """return a description for a result set"""
    description = []
    for term in selected:
        description.append(term.get_type(solution, args))
    return description

def _selection_idx_type(i, rqlst, args):
    """try to return type of term at index `i` of the rqlst's selection"""
    for select in rqlst.children:
        term = select.selection[i]
        for solution in select.solutions:
            try:
                ttype = term.get_type(solution, args)
                if ttype is not None:
                    return ttype
            except CoercionError:
                return None
