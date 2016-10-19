__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

import pytest
from simr.Configuration.Configuration import Configuration

def test_simple_config():
    Configuration("Tests/simple_config.xml")

def test_cyclic_config():
    with pytest.raises(RuntimeWarning):
        Configuration("Tests/cyclic_config.xml")
