#!/usr/bin/env python

from setuptools import setup

setup(
    name='python-ultramemcached',
    version='0.0.2',
    install_requires=['umemcache'],
    author='Nicholas Serra',
    author_email='nick@528hazelwood.com',
    license='MIT License',
    url='https://github.com/nicholasserra/python-ultramemcached/',
    keywords='python memcache memcached ultramemcached ultramemcache',
    description='A drop in replacement for python-memcached that uses ultramemcache',
    long_description=open('README.md').read(),
    download_url="https://github.com/nicholasserra/python-ultramemcached/zipball/master",
    py_modules=["ultramemcache"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ]
)