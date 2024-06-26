﻿from os.path import abspath, dirname, join
from setuptools import find_packages, setup

working_dir = abspath(dirname(__file__))

with open(join(working_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lnwza',
    version='0.0.20',
    license='MIT',
    description='lnwza by hexs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='hexs',
    author_email='zxjq97@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pip=lnwza.pipp:pipp',
        ],
    },
)

# python setup.py sdist bdist_wheel
# twine upload dist/*