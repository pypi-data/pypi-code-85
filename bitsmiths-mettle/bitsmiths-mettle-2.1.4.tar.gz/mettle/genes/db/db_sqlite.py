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

from .database        import Database
from .gen_sql         import GenSql
from .gen_sql_sqlite  import GenSqlite


class DBSqlite(Database):

    def __init__(self):
        Database.__init__(self)


    def name(self) -> str:
        return 'sqlite'


    def _db_generator(self) -> GenSql:
        return GenSqlite()


    def _sequence_pre_insert(self) -> bool:
        return False


    def _sequence_post_insert(self) -> bool:
        return True


    def _sql_insert(self, gen_info: dict) -> str:
        sql = 'insert into %s (' % gen_info['table'].name

        comma = ''

        for f in gen_info['table'].columns:
            sql += '%s%s\n' % (comma, f.name)
            comma = '   ,'

        sql += ') values ('
        comma = ''

        for f in gen_info['table'].columns:
            if f.type.startswith('seq'):
                sql += '%sNULL\n' % comma
            else:
                sql += '%s:%s\n' % (comma, f.name)

            comma = '   ,'

        sql += ')'

        return sql
