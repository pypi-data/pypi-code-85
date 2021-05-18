import os
from setuptools import (
    find_packages,
    setup,
)

version = {}
with open("./oidc_provider/version.py") as fp:
    exec(fp.read(), version)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webidoidc-provider',
    version=version['__version__'],
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='WEBID - OIDC Provider implementation for Django.',
    long_description='https://git.startinblox.com/djangoldp-packages/django-webidoidc-provider',
    url='https://git.startinblox.com/djangoldp-packages/django-webidoidc-provider',
    author='Juan Ignacio Fiorentino + Startin\'blox Team',
    author_email='support@startinblox.com',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='runtests.runtests',
    tests_require=[
        'mock>=2.0.0',
    ],

    install_requires=[
        'pyjwkest>=1.3.0',
        'pyjwt[crypto]~=2.1',
    ]
)
