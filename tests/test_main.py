import pytest
from main import main
import sys


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


def test_main():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = ["main.py"]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_main_help():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = ["main.py", "-h"]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_main_no_config():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        sys.argv = ["main.py", "-m", "1"]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

def test_main_echo():
    sys.argv = ["main.py", "tests/config/main_echo.xml"]
    main()

def test_main_maxworkers_echo():
    sys.argv = ["main.py", "-m", "1", "tests/config/main_echo.xml"]
    main()

#def test_main_interactive_echo():
#    sys.argv = ["main.py", "-i", "tests/config/main_echo.xml"]
#    main()
