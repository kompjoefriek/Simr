import pytest
from simr.Configuration.Configuration import Configuration


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


def test_no_config():
    with pytest.raises(TypeError):
        Configuration()


def test_variables_simple_config():
    Configuration("tests/variables_simple_config.xml")


def test_variables_complex_config():
    Configuration("tests/variables_complex_config.xml")


def test_variables_cyclic_config():
    with pytest.raises(RuntimeWarning):
        Configuration("tests/variables_cyclic_config.xml")


def test_variables_date_config():
    Configuration("tests/variables_date_config.xml")
