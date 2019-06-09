import os
from setuptools import setup, find_packages

install_reqs = [line.strip() for line in open('requirements.txt').readlines()]

setup(
    name='MySB_datatraffic',
    version='1.0',
    description='MySoftBank dataTraffic',
    url='https://github.com/0x0u/dataTraffic',
    author='m0zu',
    author_email='m0zurillex@gmail.com',
    keywords='Python3 MySoftBank',
    packages=find_packages(),
    install_requires=install_reqs,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=['Programming Language :: Python :: 3.6']
)
