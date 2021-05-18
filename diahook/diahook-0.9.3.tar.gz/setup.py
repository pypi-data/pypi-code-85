"""
    Diahook

    The Diahook server API documentation  # noqa: E501

    The version of the OpenAPI document: 0.8.1
    Generated by: https://openapi-generator.tech
"""

import os
from setuptools import setup, find_packages  # noqa: H301

NAME = "diahook"
VERSION = "0.9.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=NAME,
    version=VERSION,
    description="Diahook",
    author="Diahook",
    author_email="development@diahook.com",
    url="https://www.diahook.com",
    license="SEE LICENSE IN LICENSE.md",
    keywords=[
        "diahook",
        "webhooks",
    ],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
)
