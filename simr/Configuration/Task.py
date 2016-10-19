from subprocess import check_call, CalledProcessError


"""
This file contains the class Task, meant to encapsulate a given task as configured.
"""
__author__ = 'Sander Krause <sanderkrause@gmail.com>'
__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


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
        command_and_parameters = [self.command]
        command_and_parameters.extend(self.parameters)
        try:
            check_call(command_and_parameters)
        except FileNotFoundError as e:
            print("Error in task({}): {}".format(self.name, e.strerror))
        except CalledProcessError as e:
            print("Error in task({}): exit code {}".format(self.name, e.returncode))

    def __repr__(self):
        import json

        return "Task {{\n  name:\"{}\",\n  command: \"{}\",\n  parameters: {}\n  output: {},\n}}" \
            .format(self.name, self.command, json.dumps(self.parameters), self.output)\
