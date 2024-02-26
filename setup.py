# -*- coding: utf-8 -*-
"""setup.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rkijkBKpOtwRDpIDw_c3bsIDJQ73PU71
"""

from setuptools import setup, find_packages

setup(
    name='AutoEDA',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='Automatic Exploratory Data Analysis (EDA) library',
    author='Prabhmeet Singh',
    author_email='shailinder74@gmail.com',
    url='https://github.com/prabhmeet24/AutoEDA',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scipy',
        'scikit-learn',
        'prettytable',
    ],
)