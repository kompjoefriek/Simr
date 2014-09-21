"""
This file contains the class Task, currently not used (Configuration.Task is used instead)
"""
__author__ = 'Sander Krause <sanderkrause@gmail.com>'

from subprocess import call


class Task:

    command = None
    input = None
    output = None
    name = None

    def __init__(self, config):
        if "command" in config:
            self.command = config["command"]
        if "input" in config:
            self.input = config["input"]
        if "output" in config:
            self.output = config["output"]
        if "name" in config:
            self.name = config["name"]

    def run(self):
        # TODO: handle input / output redirects properly
        call(self.command)