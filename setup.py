"""The setup file only exists to be able to build the docs on readthedocs!"""
from setuptools import find_packages, setup

with open("README.md") as stream:
    long_description = stream.read()

REQUIREMENTS = [
    "ascii-canvas>=1.2.2",
    "ordereddict>=1.1",
    "strip-hints>=0.1.7",
    'futures; python_version == "2.7"',
]

setup(
    name="flowpipe",
    version="0.9.0",
    author="Paul Schweizer",
    author_email="paulschweizer@gmx.net",
    description="Lightweight flow-based programming framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PaulSchweizer/flowpipe",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python",
    ],
)
