# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crwaler',
    version='0.1.0',
    description='Crwaler for researchgate',
    long_description=readme,
    author='Samit Sharma',
    author_email='zz-sasharma@fullerton.edu',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

