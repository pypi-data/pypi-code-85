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

import base64
import datetime
import uuid

from mettle.io.py_list_writer import PyListWriter
from mettle.io.util           import Util


class PyJsonListWriter(PyListWriter):
    """
    Write a mettle object into a python list, converts datetimes to std json datetime strings.
    """

    def __init__(self, stream, tzinfo=None):
        """
        Constructor

        :param stream: (mettle.io.IStream) The target ListStream to write to.
        """
        PyListWriter.__init__(self, stream)
        self._tzinfo = tzinfo


    def _write_field(self, field: str, v, ftype: type):
        if v is None:
            if ftype == float:
                raise Exception('Cannot serialize object to list, [%s] field is None.' % (field))

        elif ftype != type(v):
            if ftype == bytes and isinstance(v, bytearray):
                v = base64.b64encode(v).decode('ascii')
            elif (ftype == dict or ftype == list) and v is None:
                v = None
            elif ftype == uuid.UUID and v is None:
                v = ''
            elif not isinstance(v, str) or \
                    (ftype != datetime.datetime and ftype != datetime.date and ftype != datetime.time and\
                        ftype != bytes and ftype != dict):
                raise Exception('Cannot serialize object to dictionary, [%s] field is the incorrect'
                                ' type, expected [%s] and got [%s].' % (field, str(ftype), str(type(v))))

        else:
            if ftype == datetime.datetime:
                v = Util.datetime_2_json(field, v, self._tzinfo)
            elif ftype == datetime.date:
                v = Util.date_2_json(field, v)
            elif ftype == datetime.time:
                v = Util.time_2_json(field, v)
            elif ftype == uuid.UUID:
                v = Util.guid_2_json(field, v)
            elif ftype == bytes:
                v = base64.b64encode(v).decode('ascii')

        self._stream.write(v)
