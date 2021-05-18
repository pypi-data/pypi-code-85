# coding: utf-8
# Modified Work: Copyright (c) 2018, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

######################## BEGIN LICENSE BLOCK ########################
# Contributor(s):
#   Dan Blanchard
#   Ian Cordasco
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

import sys


if sys.version_info < (3, 0):
    PY2 = True
    PY3 = False
    base_str = (str, unicode)
    text_type = unicode
else:
    PY2 = False
    PY3 = True
    base_str = (bytes, str)
    text_type = str
