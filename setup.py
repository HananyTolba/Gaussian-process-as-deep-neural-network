#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = "Hanany Tolba"
# __copyright__ = "Copyright 2020, Guassian Process as Deep Learning Model Project"
# __credits__ = "Hanany Tolba"
# __license__ = "Apache License 2.0"
# __version__ ="0.1"
# __maintainer__ = "Hanany Tolba"
# __email__ = "hananytolba@yahoo.com"
# __status__ = "4 - Beta"



"""
Fast and easy gaussian process regression using deep learning with tensorflow


"""




from setuptools import setup, find_packages

# import pkg_resources  # part of setuptools
#version = pkg_resources.require("makeprediction")[0].version
#version = "0.0.1"
#import gprbytf

with open('makeprediction/version.py') as f:
    exec(f.read())

# try:
#     import pypandoc
#     long_description = pypandoc.convert('README.md', 'rst')
# except(IOError, ImportError):
#     long_description = open('README.md').read()

setup(
    name='makeprediction',         # How you named your package folder (MyLib)
    packages=['makeprediction'],
    # packages=find_packages(where='src'),
    # package_dir='gprbytf',   # Chose the same as "name"
    # version = gprbytf.__version__, #"0.0.1",      # Start with a small
    # number and increase it with every change you make
    version=__version__,      # Start with a small number and increase it with every change you make

    # Chose a license from here:
    # https://help.github.com/articles/licensing-a-repository
    license="GPLv3",
    description="Fast and easy gaussian process regression for time series prediction",
    author=__author__, 
    #long_description = long_description,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',                 # Type in your name
    author_email=__email__,
    # Provide either the link to your github or to your website
    url='https://github.com/HananyTolba/MakePrediction.git',
    download_url='https://github.com/HananyTolba/MakePrediction.git',    # I explain this later on
    keywords=[
        'Gaussian Process Regression',
        'Time series prediction',
        'Deep Learning',
        'Machine Learning'],
    platforms= [],
    install_requires=[            # I get to this in a second
        #"numpy<1.19.0,>=1.16.0",
        'numpy',
        "colorama",
        "tqdm",
        "termcolor",
        "scipy",
        "requests",
        "joblib",
        "matplotlib",
        "pandas",
        "pytest",
        "plotly",
        "dash",
        "dash-bootstrap-components",
        
        #"matplotlib",
        # only for the demo
    ],
    #package_data={'makeprediction': ['keras_600/*']},
    #python_requires=">=3.5, <=3.8.5",
    python_requires=">=3.5",
    include_package_data=True,

    # classifiers=[
    #     "Programming Language :: Python",
    #     "Development Status :: 1 - Planning",
    #     "License :: OSI Approved",
    #     "Natural Language :: French",
    #     "Operating System :: OS Independent",
    #     "Programming Language :: Python :: 2.7",
    #     "Topic :: Communications",
    # ],



    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as
        # the current state of your package
        'Development Status :: 4 - Beta',
        #'License :: OSI Approved :: Apache Software License',
        #'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Natural Language :: English',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
