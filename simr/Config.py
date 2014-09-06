__author__ = 'Sander Krause <sanderkrause@gmail.com>'


try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

from simr.Variable.Variable import Variable
from pprint import pprint


class Config:

    config = None
    variables = []
    tasks = []

    def __init__(self, filename):
        document = etree.parse(filename)
        self.config = document.getroot()
        # parse variables
        variable_root = self.config.find('variables')
        if variable_root is not None:
            for variable_element in variable_root.findall('variable'):
                variable = {
                    "name": variable_element.get("name"),
                    "value": variable_element.get("value"),
                }
                self.variables.append(Variable(variable))
        for variable in self.variables:
            variable.check_references(self.variables)
        for variable in self.variables:
            variable.resolve(self.variables, [])
        for variable in self.variables:
            if not variable.depends_name is None and not len(variable.depends_name) == 0:
                print("Variable \"%s\" could not be resolved! Depends on: %s" % (variable.name, variable.depends_name))

        # parse tasks
        task_root = self.config.find('tasks')
        if task_root is not None:
            for task_element in task_root.findall('task'):
                task = {
                    "command": task_element.find("command").text,
                    "input": [],
                    "output": None,
                    "name": task_element.get("name")
                }
                if task_element.find("output") is not None and task_element.find("output").find('redirect') is not None:
                    task["output"] = task_element.find("output").find("redirect").get("target")
                if task_element.find("input") is not None and task_element.find("input").find('parameter') is not None:
                    parameters = {parameter.get('key'): parameter.get('value') for parameter in task_element.find("input").findall('parameter')}
                    task["input"] = parameters
                self.tasks.append(task)

    def get_variables(self):
        return self.variables

    def get_tasks(self):
        return self.tasks
