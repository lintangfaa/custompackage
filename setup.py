from os import name
from sys import version
import setuptools

with open("README.md", "r") as fh :
    long_description = fh.read()

setuptools.setup(
    name = "ai_pkg",
    version = "0.0.2", 
    author = "Lintang Fauziyatu",
    author_email = "fauziyatuazmi@gmail.com",
    description = "new custom package ai_pkg, new version",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Lisence :: OSI Approve :: MIT Lisence",
        "Operating System :: OS Independent",
    ],
)