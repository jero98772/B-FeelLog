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
	version='1.0.0-Beta',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='free source minimal multilingual blog maker and manager for different blog entries and multiple blog entries , with web interface. in this blog can use images but we looking to keep it minimalism.',
	url='https://jero98772.pythonanywhere.com/',
	packages=find_packages(),
    install_requires=['Flask','deep-translator'],
    include_package_data=True,
	)
genTokenFile("data/token.txt")