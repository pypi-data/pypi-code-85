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

import time

from .generator import Generator
from .gen_sql   import GenSql


class GenSqlite(GenSql):

    def __init__(self):
        GenSql.__init__(self)

        self._field_map['bool']      = Generator.FieldMap('INTEGER')
        self._field_map['int8']      = Generator.FieldMap('INTEGER')
        self._field_map['int16']     = Generator.FieldMap('INTEGER')
        self._field_map['int32']     = Generator.FieldMap('INTEGER')
        self._field_map['int64']     = Generator.FieldMap('INTEGER')
        self._field_map['seq32']     = Generator.FieldMap('INTEGER')
        self._field_map['seq64']     = Generator.FieldMap('INTEGER PRIMARY KEY')
        self._field_map['char']      = Generator.FieldMap('CHARACTER(1)')
        self._field_map['string']    = Generator.FieldMap('VARCHAR', True)
        self._field_map['date']      = Generator.FieldMap('CHARACTER(8)')
        self._field_map['time']      = Generator.FieldMap('CHARACTER(6)')
        self._field_map['datetime']  = Generator.FieldMap('CHARACTER(14)')
        self._field_map['timestamp'] = Generator.FieldMap('CHARACTER(14)')
        self._field_map['double']    = Generator.FieldMap('NUMERIC')
        self._field_map['memblock']  = Generator.FieldMap('BLOB')
        self._field_map['uuid']      = Generator.FieldMap('CHARACTER(36)')
        self._field_map['json']      = Generator.FieldMap('VARCHAR', True)


    def _gen_message(self):
        for fh in self._all_file_handles() :
            fh.write('-- This file was generated by mettle.genes.db.GenSqlite [ver %s] on %s\n\n' % (
                self._gen_info['version'], time.asctime()))


    def _gen_header(self):
        pass


    def _genField(self, field):
        if field.type not in self._field_map:
            raise Exception('Unkown field type "%s/%s"' % (field.type, field.name))

        if self._field_map[field.type].length and field.length:
            return '%s %s(%d)' % (field.name, self._field_map[field.type].name, field.length)

        return '%s %s' % (field.name, self._field_map[field.type].name)


    def _gen_create_table(self):
        for fh in [self._sqlfh, self._dropfh] :
            fh.write('DROP TABLE IF EXISTS %s;\n\n' % self._tableName)

        for fh in [self._sqlfh, self._tablefh] :
            fh.write('CREATE TABLE %s (\n' % self._tableName)

            comma = ' '
            nn    = ''

            for f in self._gen_info['table'].columns:
                if not f.not_null:
                    nn = ''
                else:
                    nn = ' NOT NULL'

                fh.write('  %s%s%s\n' % (comma, self._genField(f), nn))
                comma = ','

            # -- Do Primary Keys
            if len(self._gen_info['table'].primary_keys) > 0:
                addKey = True

                if len(self._gen_info['table'].primary_keys) == 1:

                    pki = self._gen_info['table'].primary_keys[0]
                    col = self._gen_info['table'].columns[pki.index]

                    if col.type in ('seq32', 'seq64'):
                        addKey = False


                if addKey:
                    fh.write('  ,PRIMARY KEY (')
                    comma = ''

                    for pk in self._gen_info['table'].primary_keys:
                        fh.write('%s%s' % (comma, self._gen_info['table'].columns[pk.index].name))
                        comma = ', '

                    fh.write(')\n')

            # -- Do Foreign Keys
            if len(self._gen_info['table'].foreign_keys) > 0:
                for fk in self._gen_info['table'].foreign_keys:
                    comma = ''
                    fh.write('  ,FOREIGN KEY (')

                    for field in fk.columns:
                        fh.write('%s%s' % (comma, self._gen_info['table'].columns[field].name))
                        comma = ', '

                    fh.write(') REFERENCES %s\n' % fk.ref_table)

            fh.write(');\n\n')

            fh.write('\n')


    def _gen_sequences(self):
        pass


    def _gen_constraints(self):
        pass


    def _gen_primary_key(self):
        pass


    def _gen_foreign_keys(self):
        pass


    def _gen_unique_keys(self):
        if not len(self._gen_info['table'].unique_keys):
            return

        for fh in [self._sqlfh, self._consfh]:
            fh.write('-- UNIQUE KEY(S)\n\n')

            for uk in self._gen_info['table'].unique_keys:
                fh.write('CREATE UNIQUE INDEX %s_%s ON %s\n' % (self._gen_info['table'].name, uk.name, self._tableName))
                fh.write('(\n')

                comma = ' '
                for f in uk.columns:
                    fh.write('  %s%s\n' % (comma, self._gen_info['table'].columns[f].name))
                    comma = ','

                fh.write(');\n\n')


    def _gen_indexes(self):
        if not len(self._gen_info['table'].indexes):
            return

        for fh in [self._sqlfh, self._indexfh]:
            fh.write('-- INDEXES\n\n')

            for idx in self._gen_info['table'].indexes:
                fh.write('CREATE INDEX %s_%s ON %s\n' % (self._gen_info['table'].name, idx.name, self._tableName))
                fh.write('(\n')

                comma = ' '
                for f in idx.columns:
                    fh.write('  %s%s\n' % (comma, self._gen_info['table'].columns[f].name))
                    comma = ','

                fh.write(');\n\n')


    def _gen_trailer(self):
        pass
