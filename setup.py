#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()


setup(
    name="spiewnik",
    version="0.0.1",
    description="",
    #    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    #    long_description_content_type='text/markdown',
    url="https://github.com/michalsta/spiewniki_soft",
    author="Michał Piotr Startek",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["pypdf", "reportlab"],
    scripts=glob.glob("tools/*.py"),
    package_dir={"spiewnik": "spiewnik"},
#    package_data={"spiewniki": ["data/*.csv"]},
)
