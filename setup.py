# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from setuptools import setup, find_packages

from codecs import open
from os import path

top_srcdir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(top_srcdir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyingress',
    version='0.0.1',

    description='Python module for Niantic Ingress',
    long_description=long_description,

    url='https://gitlab.com/vicamo/python-pyingress',

    author='You-Sheng Yang',
    author_email='vicamo@gmail.com',

    license='Apache Software License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='ingress',

    packages=find_packages(),
)
