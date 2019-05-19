# import os, sys, requests
# import re
import io
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='algorithms_lee',
    version='0.1.0',
    description='Pythonic Data Structures and Algorithms',
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/liyang101010/algorithms_lee',
    author='lee',
    author_email="ly61220271@gmail.com",
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    zip_safe=False)
