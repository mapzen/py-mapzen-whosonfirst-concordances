#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.concordances',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.concordances'],
    version='0.01',
    description='Tools for working with Who\'s On First concordances',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-concordances',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-dump-concordances',
        'scripts/wof-index-concordances',
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-concordances/releases/tag/v0.01',
    license='BSD')
