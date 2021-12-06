import os
from setuptools import setup

setup(
    name = "Simr",
    version = "0.0.6",
    author = "Sander Krause, Roel van Nuland",
    author_email = "sanderkrause@gmail.com, roel@kompjoefriek.nl",
    description = ("Simr is a simulation runner written in Python 3"),
    license = "MIT",
    keywords = "taskrunner",
    url = "https://github.com/kompjoefriek/Simr",
    packages=['simr', 'tests']
)
