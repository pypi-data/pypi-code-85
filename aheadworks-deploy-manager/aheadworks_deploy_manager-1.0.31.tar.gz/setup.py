from setuptools import setup

setup(
    name='aheadworks_deploy_manager',
    version='1.0.31',
    zip_safe=True,
    packages=['aheadworks_bitbucket_manager'],
    package_dir={'aheadworks_bitbucket_manager': 'aheadworks_bitbucket_manager'},
    package_data={'aheadworks_bitbucket_manager': ['*', '*/*', '*/*/*', '*/*/*/*']},
    include_package_data=True,
    url='https://bitbucket.org/awimpl/deploy-tools',
    license='EULA',
    author='nnuser',
    author_email='sednev@aheadworks.com',
    description='deploy manager from aheadworks',
    install_requires=[
        'fire',
        'python-dateutil',
        'requests',
        'docker',
        'regex',
    ]
)
