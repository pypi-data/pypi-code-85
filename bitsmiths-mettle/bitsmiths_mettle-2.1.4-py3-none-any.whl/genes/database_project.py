# **************************************************************************** #
#                           This file is part of:                              #
#                                   METTLE                                     #
#                           https://bitsmiths.co.za                            #
# **************************************************************************** #
#  Copyright (C) 2015 - 2021 Bitsmiths (Pty) Ltd.  All rights reserved.        #
#   * https://bitbucket.org/bitsmiths_za/mettle.git                            #
#                                                                              #
#  Permission is hereby granted, free of charge, to any person obtaining a     #
#  copy of this software and associated documentation files (the "Software"),  #
#  to deal in the Software without restriction, including without limitation   #
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
#  and/or sell copies of the Software, and to permit persons to whom the       #
#  Software is furnished to do so, subject to the following conditions:        #
#                                                                              #
#  The above copyright notice and this permission notice shall be included in  #
#  all copies or substantial portions of the Software.                         #
#                                                                              #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL     #
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  #
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
#  DEALINGS IN THE SOFTWARE.                                                   #
# **************************************************************************** #

import os
import os.path
import logging

from .project import Project


class DatabaseProject(Project):
    """
    The mettle database project object.
    """
    def __init__(self, proj_path, name, version):
        """
        Constructor
        """
        Project.__init__(self, proj_path, name, version)
        self.table_list     = []
        self._loaded_tables = None


    def initialize(self):
        """
        Initialize is use be user project to initialize the database project.
        """
        logging.info('Initializing project [%s]' % self.name)

        if self.version != self.VERSION:
            raise Exception('Project version %f is not the same as Generator version %f' % (self.version, self.VERSION))

        self._load_generators()
        self._load_databases()


    def _validate_project(self):
        logging.info('Validating Project...')

        if not self.generators:
            raise Exception('No code generators have been initialized for project [%s]!' % self.name)

        if not self.databases:
            raise Exception('No databases have been initialized for project [%s]!' % self.name)

        if not self.table_list:
            raise Exception('No tables have been initialized for project [%s]!' % self.name)

        for i in range(len(self.table_list)):
            tbl   = self.table_list[i].replace('/', os.path.sep)
            tpath = os.path.join(self.project_dir, tbl)

            if not os.path.exists(tpath):
                raise Exception('Table [%s] not found for project [%s]' % (tbl, self.name))

            self.table_list[i] = tbl


    def _load_generators(self):
        """
        Loads all the code generators.
        """
        logging.info('Loading database code generators')

        self.generators = {}

        import mettle.genes.db

        for gcls in mettle.genes.db.code_generators:
            gobj = gcls()
            self.generators[gobj.name()] = gobj


    def _load_databases(self):
        """
        Loads all the database.
        """
        logging.info('Loading database generators')
        self.databases = {}

        import mettle.genes.db

        for dbcls in mettle.genes.db.database_generators:
            dbobj = dbcls()
            self.databases[dbobj.name()] = dbobj


    def generate(self, clean: bool = False, for_async: bool = False):
        self._validate_project()

        gen_info               = {}
        gen_info['version']    = str(self.VERSION)
        gen_info['proj']       = self
        gen_info['clean']      = clean
        gen_info['all_tables'] = {}

        gcnt       = 0
        async_hint = ' - Standard' if not for_async else ' - Async'

        logging.info('Generate%s - Started (%s)' % (async_hint, self.name))

        for d, dobj in sorted(self.databases.items()):
            if dobj.enabled:
                dobj.initialize_generation(gen_info)

        for g, gobj in sorted(self.generators.items()):
            if not gobj.enabled:
                logging.info('  generator (%s) disabled' % gobj.name())
                continue

            if for_async:
                if not gobj.async_enabled():
                    logging.info('  code generation (%s) not enabled' % (gobj.name()))
                    continue
            else:
                if not gobj.standard_enabled():
                    logging.info('  code generation (%s) not enabled' % (gobj.name()))
                    continue

            gcnt += 1

            logging.info('  initializing generator (%s%s)' % (gobj.name(), async_hint))

            gobj.initialize_generation(gen_info)
            gobj.prepare_schema(gen_info)
            gobj.prepare_dao(gen_info)

        if not gcnt:
            logging.info('Generate%s - Skipped, no generators enabled' % async_hint)
            return

        logging.info('  processing [%d] tables' % len(self.table_list))

        gen_info['all_tables'] = self.load_tables()

        for tname, table in sorted(gen_info['all_tables'].items()):
            for proc in table.procs:
                for fld in proc.in_fields:
                    fld._resolve(gen_info, tname, proc.name)

                for fld in proc.out_fields:
                    fld._resolve(gen_info, tname, proc.name)


        for tname, table in sorted(gen_info['all_tables'].items()):
            logging.info('    loading table [%s]' % tname)

            gen_info['table'] = table

            for g, gobj in sorted(self.generators.items()):
                if not gobj.enabled:
                    continue

                if for_async:
                    if not gobj.async_enabled():
                        continue

                    if gobj.standard_enabled() and gobj.dest_dir_async() == gobj.dest_dir_standard():
                        continue

                    gobj.async_toggle(True)
                    gobj.generate_tables(gen_info)
                else:
                    if not gobj.standard_enabled():
                        continue

                    gobj.async_toggle(False)
                    gobj.generate_tables(gen_info)


            for d, dobj in sorted(self.databases.items()):
                if dobj.enabled:
                    dobj.generate(gen_info, self.generators, for_async)


        for d, dobj in sorted(self.databases.items()):
            if dobj.enabled:
                dobj.generate(gen_info, self.generators, for_async, True)

        for g, gobj in sorted(self.generators.items()):
            if not gobj.enabled:
                continue

            if for_async:
                if not gobj.async_enabled():
                    continue

                gobj.async_toggle(True)
            else:
                if not gobj.standard_enabled():
                    continue

                gobj.async_toggle(False)

            gobj.close_dao(gen_info)
            gobj.close_schema(gen_info)
            gobj.finalize_generation(gen_info)

        logging.info('Generate%s - Done(%s)' % (async_hint, self.name))


    def load_tables(self, refresh: bool = False):
        if not refresh and self._loaded_tables:
            return self._loaded_tables

        from mettle.genes import service

        self._loaded_tables = {}

        for t in self.table_list:
            logging.info('    reading table [%s]' % t)
            table = service.mettle_obj_load(os.path.join(self.project_dir, t), 'Mettle.DB.Table')
            self._loaded_tables[table.name] = table

        return self._loaded_tables
