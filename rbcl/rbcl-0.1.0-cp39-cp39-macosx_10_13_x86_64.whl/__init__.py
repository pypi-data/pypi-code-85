# Copyright 2013 Donald Stufft and individual contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

import sys
import warnings

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]

__title__ = "PyNaCl"
__summary__ = (
    "Python binding to the Networking and Cryptography (NaCl) " "library"
)
__uri__ = "https://github.com/pyca/pynacl/"

__version__ = "1.5.0.dev1"

__author__ = "The PyNaCl developers"
__email__ = "cryptography-dev@python.org"

__license__ = "Apache License 2.0"
__copyright__ = "Copyright 2013-2018 {0}".format(__author__)


if sys.version_info[0] == 2:
    warnings.warn(
        "Python 2 is no longer supported by the Python core team. Support for "
        "it is now deprecated in PyNaCl, and will be removed in the "
        "next release.",
        DeprecationWarning,
        stacklevel=2,
    )
