# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['har2tree']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'ete3>=3.1.2,<4.0.0',
 'filetype>=1.0.7,<2.0.0',
 'lxml>=4.6.3,<5.0.0',
 'numpy>=1.20.3,<2.0.0',
 'publicsuffix2>=2.20191221,<3.0',
 'six>=1.16.0,<2.0.0',
 'w3lib>=1.22.0,<2.0.0']

extras_require = \
{'docs': ['Sphinx>=3.5.3,<4.0.0', 'myst-parser>=0.14.0']}

setup_kwargs = {
    'name': 'har2tree',
    'version': '1.5.9',
    'description': 'HTTP Archive (HAR) to ETE Toolkit generator',
    'long_description': '[![Documentation Status](https://readthedocs.org/projects/har2tree/badge/?version=latest)](https://har2tree.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/Lookyloo/har2tree/branch/master/graph/badge.svg)](https://codecov.io/gh/Lookyloo/har2tree)\n\nHar2Tree\n========\n\n\nThis package generate a tree out of a HAR dump.\n\n\nInstallation\n============\n\n```bash\npip install har2tree\n```\n',
    'author': 'Raphaël Vinot',
    'author_email': 'raphael.vinot@circl.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Lookyloo/har2tree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
