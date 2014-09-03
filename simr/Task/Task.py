__author__ = 'Sander Krause <sanderkrause@gmail.com>'

from subprocess import call


class Task:

    command = None
    input = None
    output = None

    def __init__(self, config):
        if "command" in config:
            self.command = config.command
        if "input" in config:
            self.input = config.input
        if "output" in config:
            self.output = config.output

    def run(self):
        # TODO: handle input / output redirects properly
        call(self.command)