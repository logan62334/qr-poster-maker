#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################
# File Name: setup.py
# Author: logan62334
# Mail: logan62334@gmail.com
# Created Time:  2019-02-26 20:25:34 PM
#############################################

from setuptools import setup, find_packages

setup(
    name="qrmaker",
    version="1.0.3",
    description="qr code poster maker",
    long_description=open("README.md").read(),
    license="MIT Licence",

    author="logan62334",
    author_email="logan62334@gmail.com",
    url="https://github.com/logan62334/qr-poster-maker.git",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=["Pillow", "click"],
    entry_points={
        'console_scripts': ['maker = maker.maker:qrmaker']
    },
)
