# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resume_pycli']

package_data = \
{'': ['*'],
 'resume_pycli': ['themes/base/*',
                  'themes/stackoverflow/*',
                  'themes/stackoverflow/partials/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'click>=8.0.0,<9.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'pdfkit>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['resume = resume_pycli.script:cli',
                     'resumepy = resume_pycli.script:cli']}

setup_kwargs = {
    'name': 'resume-pycli',
    'version': '1.2.0',
    'description': 'CLI tool to easily setup a new resume',
    'long_description': '# resume-pycli\n\nCLI tool to build a beautiful resume from a [JSON\nResume](https://jsonresume.org/) file.\n\nThis is a Python port of\n[resume-cli](https://github.com/jsonresume/resume-cli).\n\n[![builds.sr.ht status](https://builds.sr.ht/~nka/resume-pycli.svg)](https://builds.sr.ht/~nka/resume-pycli)\n[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/resume-pycli)](https://libraries.io/pypi/resume-pycli)\n[![PyPI Version](https://img.shields.io/pypi/v/resume-pycli?color=4DC71F&logo=python&logoColor=fff)](https://pypi.org/project/resume-pycli/)\n[![AUR Version](https://img.shields.io/aur/version/resume-pycli?logo=linux&logoColor=fff)](https://aur.archlinux.org/packages/resume-pycli/)\n\n## Features\n\n* Validate your `resume.json` against schema\n* Export your resume to HTML\n* Export your resume to PDF\n* Customize the theme of your HTML and PDF exports\n* Run a local HTTP server to preview the HTML export\n* Create an inital `resume.json` with placeholder values to get started\n\n## Installation\n\nWith [pipx](https://pipxproject.github.io/pipx/):\n\n```\npipx install resume-pycli\n```\n\nWith [brew](https://brew.sh/):\n\n```\nbrew install nikaro/tap/resume-pycli\n```\n\nOn ArchLinux from the [AUR](https://aur.archlinux.org/packages/resume-pycli/):\n\n```\nyay -S resume-pycli\n\n# or without yay\ngit clone https://aur.archlinux.org/resume-pycli.git\ncd resume-pycli/\nmakepkg -si\n```\n\n## Usage\n\n```\nUsage: resume [OPTIONS] COMMAND [ARGS]...\n\n  CLI tool to easily setup a new resume.\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  export    Export to HTML and PDF.\n  init      Initialize a resume.json file.\n  serve     Serve resume.\n  validate  Validate resume\'s schema.\n```\n\nExport your resume with a custom theme, for exemple one located in\n`./themes/my-beautiful-theme`:\n\n```\nresume export --theme my-beautiful-theme\n```\n\nIf you want to export custom version of your resume, for example a shorter one\nlocated at `./resume.short.json`, to PDF only:\n\n```\nresume export --resume resume.short.json --pdf\n```\n\n## Themes\n\nYou can put your theme in `themes/<name>` next to your `resume.json` file. It\nuses [Jinja2](https://jinja2docs.readthedocs.io/en/stable/) as templating\nengine. Take a look at the [small\ndemo](https://git.sr.ht/~nka/resume-pycli/tree/main/item/src/resume_pycli/themes/base/)\nthat you can take as example to write your own.\n\nIt is not compatible with ["official" community\nthemes](https://jsonresume.org/themes/) and at the moment i have not included a\nbeautiful one.\n',
    'author': 'Nicolas Karolak',
    'author_email': 'nicolas@karolak.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sr.ht/~nka/resume-pycli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
