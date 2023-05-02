import pytest
from simr.Configuration.Task import Task


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

def test_getters():
    task = Task("name", "command", ["param1", "param2"], "output")
    assert task.get_name() == "name"
    assert task.get_command() == "command"
    assert task.get_parameters() == ["param1", "param2"]
    assert task.get_output() == "output"

def test_representation():
    task = Task("name", "command", ["param1", "param2"], "output")
    assert repr(task) == "Task {\n  name:\"name\",\n  command: \"command\",\n  parameters: [\"param1\", \"param2\"]\n  output: output,\n}"

def test_run_unknown():
    task = Task(None, "unknown")
    task.run()

def test_run_exitcode():
    task = Task(None, "/bin/false")
    task.run()
