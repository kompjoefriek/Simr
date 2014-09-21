"""
This file contains the class Task, meant to encapsulate a given task as configured.
"""
__author__ = 'Sander Krause <sanderkrause@gmail.com>'

from subprocess import check_call


class Task:
    """
    Encapsulate a task as configured in the configuration file.
    """

    name = None
    command = None
    parameters = None
    output = None
    no_name = 0

    def __init__(self, name, command, parameters=[], output=None):
        if name is None:
            Task.no_name += 1
            self.name = "No Name {}".format(Task.no_name)
        else:
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

    def run(self):
        # TODO: handle input / output redirects properly

        command_and_parameters = list(self.command)
        command_and_parameters.extend(self.parameters)
        try:
            check_call(command_and_parameters)
        except FileNotFoundError:
            pass

    def __repr__(self):
        import json

        return "Task {{\n  name:\"{}\",\n  command: \"{}\",\n  output: {},\n  parameters: {}\n}}" \
            .format(self.name, self.command, self.output, json.dumps(self.parameters))