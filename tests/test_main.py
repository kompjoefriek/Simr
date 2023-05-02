import pytest
from main import main
import sys


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

STARTING_FILE = "main.py"

def test_main():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = [STARTING_FILE]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_main_help():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = [STARTING_FILE, "-h"]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_main_no_config():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = [STARTING_FILE, "-m", "1"]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

def test_main_echo():
    sys.argv = [STARTING_FILE, "tests/config/main_echo.xml"]
    main()

def test_main_maxworkers_echo():
    sys.argv = [STARTING_FILE, "-m", "1", "tests/config/main_echo.xml"]
    main()

#def test_main_interactive_echo():
#    sys.argv = [STARTING_FILE, "-i", "tests/config/main_echo.xml"]
#    main()
