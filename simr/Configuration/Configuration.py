try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

import shlex
import time

from simr.Configuration.Variable import Variable
from simr.Configuration.Task import Task


# This file contains the Configuration class, used to encapsulate the XML configuration file config/simr.xml.
__author__ = 'Sander Krause <sanderkrause@gmail.com>'
__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'
__author__ = 'Luke Buitendijk <lukebuitendijk@gmail.com>'


class Configuration:
    # Provide an encapsulated way to parse the configuration file and access its properties.

    config = None
    variables = []
    tasks = []

    def __init__(self, filename):
        try:
            document = etree.parse(filename)
            self.config = document.getroot()
        except etree.ParseError as e:
            row, column = e.position
            raise RuntimeError("Parsing xml \"{}\" failed on line {}, column {}"
                               .format(filename, row, column))

        # parse variables
        self.variables = []

        # Add custom date variable
        dateVariable = {
            "name": "DATE",
            "value": time.strftime("%Y%m%d"),
        }
        self.variables.append(Variable(**dateVariable))
        timeVariable = {
            "name": "TIME",
            "value": time.strftime("%H%M%S"),
        }
        self.variables.append(Variable(**timeVariable))

        self.parse_variables()
        # parse tasks
        self.tasks = []
        self.parse_tasks()

    def parse_variables(self):
        # Parse the variables from the configuration, and fill the list with Variable objects.
        if self.config is None:
            raise RuntimeError('Attempting to parse empty configuration')
        variable_root = self.config.find('variables')
        if variable_root is not None:
            for variable_element in variable_root.findall('variable'):
                variable = {
                    "name": variable_element.get("name"),
                    "value": variable_element.get("value"),
                }
                self.variables.append(Variable(**variable))
        for variable in self.variables:
            variable.check_references(self.variables)
        for variable in self.variables:
            variable.resolve(self.variables, [])
        for variable in self.variables:
            if variable.depends_name is not None and not len(variable.depends_name) == 0:
                raise RuntimeWarning("Variable \"{}\" could not be resolved! Depends on: {}"
                                     .format(variable.name, variable.depends_name))

    def parse_tasks(self):
        # Parse the tasks from the configuration, and fill the list with Task objects.
        if self.config is None:
            raise RuntimeError('Attempting to parse empty configuration')
        task_root = self.config.find('tasks')
        if task_root is not None:
            for task_element in task_root.findall('task'):
                command = task_element.find("command").text
                # apply variables to command
                command = Variable.resolve_value(self.variables, command)
                # split command and arguments
                command_list = shlex.split(command)
                task = {
                    "command": command_list[0],
                    "parameters": command_list[1:],
                    "output": None,
                    "name": task_element.get("name")
                }
                if task_element.find("output") is not None and task_element.find("output").find('redirect') is not None:
                    task["output"] = task_element.find("output").find("redirect").get("target")
                if task_element.find("input") is not None and task_element.find("input").find('parameter') is not None:
                    parameters = {
                        parameter.get('name'): parameter.get('value')
                        for parameter in task_element.find("input").findall('parameter')
                    }
                    task["parameters"] = parameters
                self.tasks.append(Task(**task))

    def get_variables(self):
        # Get the parsed variables from the configuration.
        return self.variables

    def get_tasks(self):
        # Get the parsed tasks from the configuration.
        return self.tasks
