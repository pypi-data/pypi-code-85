#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import subprocess
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install

NAME = "diffeqtorch"
DESCRIPTION = "DifferentialEquations.jl with PyTorch."
URL = "https://github.com/sbi-benchmark/diffeqtorch"
EMAIL = "mail@jan-matthis.de"
AUTHOR = "Jan-Matthis Lueckmann"
REQUIRES_PYTHON = ">=3.6.0, <3.9"

REQUIRED = ["julia", "opt_einsum", "torch"]

EXTRAS = {
    "dev": [
        "autoflake",
        "black",
        "flake8",
        "gitpython",
        "ipdb",
        "isort",
        "nbstripout",
        "pre-commit",
        "pylint",
        "pytest",
    ],
    "examples": ["jupyter", "matplotlib"],
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
with open(os.path.join(here, project_slug, "__version__.py")) as f:
    exec(f.read(), about)


class DevelopCommand(develop):
    def run(self):
        develop.run(self)


class InstallCommand(install):
    def run(self):
        install.run(self)


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    cmdclass={
        "develop": DevelopCommand,
        "install": InstallCommand,
        "upload": UploadCommand,
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
