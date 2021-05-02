#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
from core.tools.webutils import genTokenFile
from setuptools import setup, find_packages
setup(
	name='B→FeelLog',
	version='1.0.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='proyect for organize a blog in a better way that write all in html... ',
	url='https://jero98772.pythonanywhere.com/blog.html',
	packages=find_packages(),
    install_requires=['Flask','deep-translator'],
    include_package_data=True,
	)
genTokenFile("data/token.txt")