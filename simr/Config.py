__author__ = 'Sander Krause <sanderkrause@gmail.com>'


try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree


class Config:

    config = None
    tasks = []

    def __init__(self, filename):
        document = etree.parse(filename)
        self.config = document.getroot()
        taskRoot = self.config.find('tasks')
        if taskRoot is not None:
            for taskElement in taskRoot.findall('task'):
                task = {
                    "command": taskElement.find("command").text,
                    "input": [],
                    "output": None
                }
                if taskElement.find("output") is not None and taskElement.find("output").find('redirect') is not None:
                    task["output"] = taskElement.find("output").find("redirect").get("target")
                if taskElement.find("input") is not None and taskElement.find("input").find('parameter') is not None:
                    parameters = {parameter.get('key'): parameter.get('value') for parameter in taskElement.find("input").findall('parameter')}
                    task["input"] = parameters
                self.tasks.append(task)

    def get_tasks(self):
        return self.tasks