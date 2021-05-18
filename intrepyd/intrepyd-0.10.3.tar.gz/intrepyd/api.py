# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_api')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_api')
    _api = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_api', [dirname(__file__)])
        except ImportError:
            import _api
            return _api
        try:
            _mod = imp.load_module('_api', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _api = swig_import_helper()
    del swig_import_helper
else:
    import _api
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

INT_ENGINE_RESULT_UNKNOWN = _api.INT_ENGINE_RESULT_UNKNOWN
INT_ENGINE_RESULT_REACHABLE = _api.INT_ENGINE_RESULT_REACHABLE
INT_ENGINE_RESULT_UNREACHABLE = _api.INT_ENGINE_RESULT_UNREACHABLE

def mk_ctx():
    """mk_ctx() -> Int_ctx"""
    return _api.mk_ctx()

def del_ctx(ctx):
    """
    del_ctx(Int_ctx ctx)

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.del_ctx(ctx)

def throw_exception(msg):
    """
    throw_exception(char const * msg)

    Parameters
    ----------
    msg: char const *

    """
    return _api.throw_exception(msg)

def clear_exception():
    """clear_exception()"""
    return _api.clear_exception()

def check_exception():
    """check_exception() -> char *"""
    return _api.check_exception()

def push_namespace(ctx, name):
    """
    push_namespace(Int_ctx ctx, char const * name)

    Parameters
    ----------
    ctx: Int_ctx
    name: char const *

    """
    return _api.push_namespace(ctx, name)

def pop_namespace(ctx):
    """
    pop_namespace(Int_ctx ctx)

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.pop_namespace(ctx)

def mk_engine_bmc(ctx):
    """
    mk_engine_bmc(Int_ctx ctx) -> Int_engine_bmc

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_engine_bmc(ctx)

def set_bmc_current_depth(engine, depth):
    """
    set_bmc_current_depth(Int_engine_bmc engine, unsigned int depth)

    Parameters
    ----------
    engine: Int_engine_bmc
    depth: unsigned int

    """
    return _api.set_bmc_current_depth(engine, depth)

def set_bmc_optimize(engine):
    """
    set_bmc_optimize(Int_engine_bmc engine)

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.set_bmc_optimize(engine)

def set_bmc_allow_targets_at_any_depth(engine):
    """
    set_bmc_allow_targets_at_any_depth(Int_engine_bmc engine)

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.set_bmc_allow_targets_at_any_depth(engine)

def set_bmc_use_induction(engine):
    """
    set_bmc_use_induction(Int_engine_bmc engine)

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.set_bmc_use_induction(engine)

def set_bmc_use_attack_path_axioms(ctx, engine, source, target):
    """
    set_bmc_use_attack_path_axioms(Int_ctx ctx, Int_engine_bmc engine, Int_net source, Int_net target)

    Parameters
    ----------
    ctx: Int_ctx
    engine: Int_engine_bmc
    source: Int_net
    target: Int_net

    """
    return _api.set_bmc_use_attack_path_axioms(ctx, engine, source, target)

def bmc_add_target(ctx, engine, target):
    """
    bmc_add_target(Int_ctx ctx, Int_engine_bmc engine, Int_net target)

    Parameters
    ----------
    ctx: Int_ctx
    engine: Int_engine_bmc
    target: Int_net

    """
    return _api.bmc_add_target(ctx, engine, target)

def bmc_add_watch(ctx, engine, watch):
    """
    bmc_add_watch(Int_ctx ctx, Int_engine_bmc engine, Int_net watch)

    Parameters
    ----------
    ctx: Int_ctx
    engine: Int_engine_bmc
    watch: Int_net

    """
    return _api.bmc_add_watch(ctx, engine, watch)

def bmc_reach_targets(engine):
    """
    bmc_reach_targets(Int_engine_bmc engine) -> Int_engine_result

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.bmc_reach_targets(engine)

def bmc_remove_last_reached_targets(engine):
    """
    bmc_remove_last_reached_targets(Int_engine_bmc engine)

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.bmc_remove_last_reached_targets(engine)

def bmc_last_reached_targets_number(engine):
    """
    bmc_last_reached_targets_number(Int_engine_bmc engine) -> unsigned int

    Parameters
    ----------
    engine: Int_engine_bmc

    """
    return _api.bmc_last_reached_targets_number(engine)

def bmc_last_reached_target(engine, n):
    """
    bmc_last_reached_target(Int_engine_bmc engine, unsigned int n) -> Int_net

    Parameters
    ----------
    engine: Int_engine_bmc
    n: unsigned int

    """
    return _api.bmc_last_reached_target(engine, n)

def bmc_get_trace(ctx, bmc, target):
    """
    bmc_get_trace(Int_ctx ctx, Int_engine_bmc bmc, Int_net target) -> Int_trace

    Parameters
    ----------
    ctx: Int_ctx
    bmc: Int_engine_bmc
    target: Int_net

    """
    return _api.bmc_get_trace(ctx, bmc, target)

def mk_engine_br(ctx):
    """
    mk_engine_br(Int_ctx ctx) -> Int_engine_br

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_engine_br(ctx)

def br_add_target(ctx, engine, target):
    """
    br_add_target(Int_ctx ctx, Int_engine_br engine, Int_net target)

    Parameters
    ----------
    ctx: Int_ctx
    engine: Int_engine_br
    target: Int_net

    """
    return _api.br_add_target(ctx, engine, target)

def br_add_watch(ctx, engine, watch):
    """
    br_add_watch(Int_ctx ctx, Int_engine_br engine, Int_net watch)

    Parameters
    ----------
    ctx: Int_ctx
    engine: Int_engine_br
    watch: Int_net

    """
    return _api.br_add_watch(ctx, engine, watch)

def br_reach_targets(engine):
    """
    br_reach_targets(Int_engine_br engine) -> Int_engine_result

    Parameters
    ----------
    engine: Int_engine_br

    """
    return _api.br_reach_targets(engine)

def br_remove_last_reached_targets(engine):
    """
    br_remove_last_reached_targets(Int_engine_br engine)

    Parameters
    ----------
    engine: Int_engine_br

    """
    return _api.br_remove_last_reached_targets(engine)

def br_last_reached_targets_number(engine):
    """
    br_last_reached_targets_number(Int_engine_br engine) -> unsigned int

    Parameters
    ----------
    engine: Int_engine_br

    """
    return _api.br_last_reached_targets_number(engine)

def br_last_reached_target(engine, n):
    """
    br_last_reached_target(Int_engine_br engine, unsigned int n) -> Int_net

    Parameters
    ----------
    engine: Int_engine_br
    n: unsigned int

    """
    return _api.br_last_reached_target(engine, n)

def br_get_trace(ctx, br, target):
    """
    br_get_trace(Int_ctx ctx, Int_engine_br br, Int_net target) -> Int_trace

    Parameters
    ----------
    ctx: Int_ctx
    br: Int_engine_br
    target: Int_net

    """
    return _api.br_get_trace(ctx, br, target)

def trace_prepare_value_for_net(ctx, cex, net, depth):
    """
    trace_prepare_value_for_net(Int_ctx ctx, Int_trace cex, Int_net net, unsigned int depth) -> unsigned int

    Parameters
    ----------
    ctx: Int_ctx
    cex: Int_trace
    net: Int_net
    depth: unsigned int

    """
    return _api.trace_prepare_value_for_net(ctx, cex, net, depth)

def prepare_value_for_net(ctx, net):
    """
    prepare_value_for_net(Int_ctx ctx, Int_net net) -> unsigned int

    Parameters
    ----------
    ctx: Int_ctx
    net: Int_net

    """
    return _api.prepare_value_for_net(ctx, net)

def value_at(i):
    """
    value_at(unsigned int i) -> char

    Parameters
    ----------
    i: unsigned int

    """
    return _api.value_at(i)

def trace_get_max_depth(trace):
    """
    trace_get_max_depth(Int_trace trace) -> unsigned int

    Parameters
    ----------
    trace: Int_trace

    """
    return _api.trace_get_max_depth(trace)

def mk_trace(ctx):
    """
    mk_trace(Int_ctx ctx) -> Int_trace

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_trace(ctx)

def trace_set_value(ctx, trace, net, depth, value):
    """
    trace_set_value(Int_ctx ctx, Int_trace trace, Int_net net, unsigned int depth, char const * value)

    Parameters
    ----------
    ctx: Int_ctx
    trace: Int_trace
    net: Int_net
    depth: unsigned int
    value: char const *

    """
    return _api.trace_set_value(ctx, trace, net, depth, value)

def trace_get_watched_nets_number(trace):
    """
    trace_get_watched_nets_number(Int_trace trace) -> unsigned int

    Parameters
    ----------
    trace: Int_trace

    """
    return _api.trace_get_watched_nets_number(trace)

def trace_get_watched_net(trace, i):
    """
    trace_get_watched_net(Int_trace trace, unsigned int i) -> Int_net

    Parameters
    ----------
    trace: Int_trace
    i: unsigned int

    """
    return _api.trace_get_watched_net(trace, i)

def mk_simulator(ctx):
    """
    mk_simulator(Int_ctx ctx) -> Int_simulator

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_simulator(ctx)

def simulator_add_watch(ctx, simulator, watch):
    """
    simulator_add_watch(Int_ctx ctx, Int_simulator simulator, Int_net watch)

    Parameters
    ----------
    ctx: Int_ctx
    simulator: Int_simulator
    watch: Int_net

    """
    return _api.simulator_add_watch(ctx, simulator, watch)

def simulator_simulate(simulator, trace, depth):
    """
    simulator_simulate(Int_simulator simulator, Int_trace trace, unsigned int depth)

    Parameters
    ----------
    simulator: Int_simulator
    trace: Int_trace
    depth: unsigned int

    """
    return _api.simulator_simulate(simulator, trace, depth)

def mk_boolean_type(ctx):
    """
    mk_boolean_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_boolean_type(ctx)

def mk_int8_type(ctx):
    """
    mk_int8_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_int8_type(ctx)

def mk_int16_type(ctx):
    """
    mk_int16_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_int16_type(ctx)

def mk_int32_type(ctx):
    """
    mk_int32_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_int32_type(ctx)

def mk_int64_type(ctx):
    """
    mk_int64_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_int64_type(ctx)

def mk_uint8_type(ctx):
    """
    mk_uint8_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_uint8_type(ctx)

def mk_uint16_type(ctx):
    """
    mk_uint16_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_uint16_type(ctx)

def mk_uint32_type(ctx):
    """
    mk_uint32_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_uint32_type(ctx)

def mk_uint64_type(ctx):
    """
    mk_uint64_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_uint64_type(ctx)

def mk_real_type(ctx):
    """
    mk_real_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_real_type(ctx)

def mk_float16_type(ctx):
    """
    mk_float16_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_float16_type(ctx)

def mk_float32_type(ctx):
    """
    mk_float32_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_float32_type(ctx)

def mk_float64_type(ctx):
    """
    mk_float64_type(Int_ctx ctx) -> Int_type

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_float64_type(ctx)

def mk_undef(ctx):
    """
    mk_undef(Int_ctx ctx) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_undef(ctx)

def mk_true(ctx):
    """
    mk_true(Int_ctx ctx) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_true(ctx)

def mk_false(ctx):
    """
    mk_false(Int_ctx ctx) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx

    """
    return _api.mk_false(ctx)

def mk_number(ctx, value, type):
    """
    mk_number(Int_ctx ctx, char const * value, Int_type type) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    value: char const *
    type: Int_type

    """
    return _api.mk_number(ctx, value, type)

def mk_not(ctx, x):
    """
    mk_not(Int_ctx ctx, Int_net x) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net

    """
    return _api.mk_not(ctx, x)

def mk_and(ctx, x, y):
    """
    mk_and(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_and(ctx, x, y)

def mk_or(ctx, x, y):
    """
    mk_or(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_or(ctx, x, y)

def mk_xor(ctx, x, y):
    """
    mk_xor(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_xor(ctx, x, y)

def mk_ite(ctx, i, t, e):
    """
    mk_ite(Int_ctx ctx, Int_net i, Int_net t, Int_net e) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    i: Int_net
    t: Int_net
    e: Int_net

    """
    return _api.mk_ite(ctx, i, t, e)

def mk_iff(ctx, x, y):
    """
    mk_iff(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_iff(ctx, x, y)

def mk_minus(ctx, x):
    """
    mk_minus(Int_ctx ctx, Int_net x) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net

    """
    return _api.mk_minus(ctx, x)

def mk_add(ctx, x, y):
    """
    mk_add(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_add(ctx, x, y)

def mk_sub(ctx, x, y):
    """
    mk_sub(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_sub(ctx, x, y)

def mk_mul(ctx, x, y):
    """
    mk_mul(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_mul(ctx, x, y)

def mk_div(ctx, x, y):
    """
    mk_div(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_div(ctx, x, y)

def mk_mod(ctx, x, y):
    """
    mk_mod(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_mod(ctx, x, y)

def mk_eq(ctx, x, y):
    """
    mk_eq(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_eq(ctx, x, y)

def mk_leq(ctx, x, y):
    """
    mk_leq(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_leq(ctx, x, y)

def mk_lt(ctx, x, y):
    """
    mk_lt(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_lt(ctx, x, y)

def mk_geq(ctx, x, y):
    """
    mk_geq(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_geq(ctx, x, y)

def mk_gt(ctx, x, y):
    """
    mk_gt(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_gt(ctx, x, y)

def mk_neq(ctx, x, y):
    """
    mk_neq(Int_ctx ctx, Int_net x, Int_net y) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    x: Int_net
    y: Int_net

    """
    return _api.mk_neq(ctx, x, y)

def mk_input(ctx, name, type):
    """
    mk_input(Int_ctx ctx, char const * name, Int_type type) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    name: char const *
    type: Int_type

    """
    return _api.mk_input(ctx, name, type)

def mk_output(arg1, net):
    """
    mk_output(Int_ctx arg1, Int_net net)

    Parameters
    ----------
    arg1: Int_ctx
    net: Int_net

    """
    return _api.mk_output(arg1, net)

def get_bit(arg1, net, bit):
    """
    get_bit(Int_ctx arg1, Int_net net, unsigned int bit) -> Int_net

    Parameters
    ----------
    arg1: Int_ctx
    net: Int_net
    bit: unsigned int

    """
    return _api.get_bit(arg1, net, bit)

def set_bit(arg1, x, bit, y):
    """
    set_bit(Int_ctx arg1, Int_net x, unsigned int bit, Int_net y) -> Int_net

    Parameters
    ----------
    arg1: Int_ctx
    x: Int_net
    bit: unsigned int
    y: Int_net

    """
    return _api.set_bit(arg1, x, bit, y)

def mk_assumption(arg1, net):
    """
    mk_assumption(Int_ctx arg1, Int_net net)

    Parameters
    ----------
    arg1: Int_ctx
    net: Int_net

    """
    return _api.mk_assumption(arg1, net)

def mk_latch(ctx, name, type):
    """
    mk_latch(Int_ctx ctx, char const * name, Int_type type) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    name: char const *
    type: Int_type

    """
    return _api.mk_latch(ctx, name, type)

def set_latch_init_next(ctx, latch, init, next):
    """
    set_latch_init_next(Int_ctx ctx, Int_net latch, Int_net init, Int_net next)

    Parameters
    ----------
    ctx: Int_ctx
    latch: Int_net
    init: Int_net
    next: Int_net

    """
    return _api.set_latch_init_next(ctx, latch, init, next)

def mk_substitute(ctx, term, new_subterm, old_subterm):
    """
    mk_substitute(Int_ctx ctx, Int_net term, Int_net new_subterm, Int_net old_subterm) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net
    new_subterm: Int_net
    old_subterm: Int_net

    """
    return _api.mk_substitute(ctx, term, new_subterm, old_subterm)

def mk_cast_to_int8(ctx, term):
    """
    mk_cast_to_int8(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_int8(ctx, term)

def mk_cast_to_int16(ctx, term):
    """
    mk_cast_to_int16(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_int16(ctx, term)

def mk_cast_to_int32(ctx, term):
    """
    mk_cast_to_int32(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_int32(ctx, term)

def mk_cast_to_uint8(ctx, term):
    """
    mk_cast_to_uint8(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_uint8(ctx, term)

def mk_cast_to_uint16(ctx, term):
    """
    mk_cast_to_uint16(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_uint16(ctx, term)

def mk_cast_to_uint32(ctx, term):
    """
    mk_cast_to_uint32(Int_ctx ctx, Int_net term) -> Int_net

    Parameters
    ----------
    ctx: Int_ctx
    term: Int_net

    """
    return _api.mk_cast_to_uint32(ctx, term)

def apitrace_dump_to_file(filename):
    """
    apitrace_dump_to_file(char const * filename)

    Parameters
    ----------
    filename: char const *

    """
    return _api.apitrace_dump_to_file(filename)

def apitrace_print_to_stdout():
    """apitrace_print_to_stdout()"""
    return _api.apitrace_print_to_stdout()

def apitrace_print_to_stderr():
    """apitrace_print_to_stderr()"""
    return _api.apitrace_print_to_stderr()
# This file is compatible with both classic and new-style classes.


