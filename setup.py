#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'botocore>=1.8.40,<1.9.0',
    'jmespath>=0.7.1,<1.0.0',
    's3transfer>=0.1.10,<0.2.0'
]


def get_version():
    init = open(os.path.join(ROOT, 'boto3_wasabi', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='boto3_wasabi',
    version=get_version(),
    description='The AWS SDK for Python',
    long_description=open('README.md').read(),
    author='Amazon Web Services',
    url='https://github.com/KalobMTaulien/boto3_wasabi',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={
        'boto3_wasabi': [
            'data/aws/resources/*.json',
            'examples/*.rst'
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
