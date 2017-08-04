"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='esri511',
    version="2.0.0",
    description="ESRI Transportation 511 Feature Collection update script",
    long_description=long_description,
    license="Apache",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Utilities"
    ],
    author="Chris Fox, John Hauck, Lindsay King",
    author_email="chris_fox@esri.com, jhauck@esri.com, lking@esri.com",
    url="https://github.com/Esri/overwrite-hosted-features",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    # This will generate executable scripts (and wrapper executable files
    # on Windows) upon installation.
    entry_points={
        'console_scripts': [
            'update511=esri511.overwrite_hosted_features:run'
        ]
    }
)