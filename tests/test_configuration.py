__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

import pytest
from simr.Configuration.Configuration import Configuration

def test_simple_config():
    Configuration("tests/simple_config.xml")

def test_cyclic_config():
    with pytest.raises(RuntimeWarning):
        Configuration("tests/cyclic_config.xml")
