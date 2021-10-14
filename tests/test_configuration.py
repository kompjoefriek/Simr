import pytest
from simr.Configuration.Configuration import Configuration


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


def test_no_config():
    with pytest.raises(TypeError):
        Configuration()


def test_non_existing_config():
    with pytest.raises(FileNotFoundError):
        Configuration("tests/config/non_existing_config.xml")


def test_empty_config():
    with pytest.raises(RuntimeError):
        Configuration("tests/config/empty_config.xml")


def test_variables_simple_config():
    Configuration("tests/config/variables_simple_config.xml")


def test_variables_complex_config():
    Configuration("tests/config/variables_complex_config.xml")


def test_variables_cyclic_config():
    with pytest.raises(RuntimeWarning):
        Configuration("tests/config/variables_cyclic_config.xml")


def test_variables_date_config():
    Configuration("tests/config/variables_date_config.xml")


def test_no_variables():
    Configuration("tests/config/main_echo.xml")


def test_task_with_input():
    Configuration("tests/config/task_with_input.xml")


def test_task_with_output():
    Configuration("tests/config/task_with_output.xml")
