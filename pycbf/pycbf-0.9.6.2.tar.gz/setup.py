# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycbf']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17']

setup_kwargs = {
    'name': 'pycbf',
    'version': '0.9.6.2',
    'description': 'An API for CBF/imgCIF Crystallographic Binary Files',
    'long_description': '# `pycbf` - CBFlib for python\n\nThis repository builds the `pycbf` portion of [CBFlib] only, as a [manylinux]\nbinary wheel installable through `pip install pycbf`.\n\nIn order to do this, it has some limitations compared to the full build of CBFlib:\n\n-   No HDF5 bindings\n-   No (custom) libTiff bindings\n-   No CBF regex capabilities\n-   No header files included - this is not intended to be used as a linking\n    target\n\nIn addition to the base 0.9.6, this has the following alterations:\n\n| Version                | Changes                                                                                                    |\n| ---------------------- | ---------------------------------------------------------------------------------------------------------- |\n| 0.9.6.0                | Regenerated SWIG bindings for Python 3 compatibility. Compiled with `SWIG_PYTHON_STRICT_BYTE_CHAR`.        |\n| ~~0.9.6.1~~            | This was an unreleased internal version.                                                                   |\n\n[cbflib]: https://github.com/yayahjb/cbflib\n[manylinux]: https://www.python.org/dev/peps/pep-0571/\n[`yayahjb/cbflib#19`]: https://github.com/yayahjb/cbflib/pull/19\n',
    'author': 'Herbert J. Bernstein',
    'author_email': 'yaya@bernstein-plus-sons.com',
    'maintainer': 'Nicholas Devenish',
    'maintainer_email': 'ndevenish@gmail.com',
    'url': 'http://www.bernstein-plus-sons.com/software/CBF/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
