"""
This file contains the class Task, meant to encapsulate a given task as configured.
"""
__author__ = 'Sander Krause <s.krause@pointerbp.nl>'


class Task:
    """
    Encapsulate a task as configured in the configuration file.
    """

    name = None
    command = None
    parameters = None
    output = None

    def __init__(self, name, command, parameters={}, output=None):
        self.name = name
        self.command = command
        self.parameters = parameters
        self.output = output

    def get_name(self):
        return self.name

    def get_command(self):
        return self.command

    def get_parameters(self):
        return self.parameters

    def get_output(self):
        return self.output

    def __repr__(self):
        import json
        return "Task {{\n  name:\"{}\",\n  command\"{}\",\n  output: {},\n  parameters: {}\n}}".format(self.name, self.command, self.output, json.dumps(self.parameters))