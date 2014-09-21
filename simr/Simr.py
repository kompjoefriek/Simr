__author__ = 'Sander Krause <sanderkrause@gmail.com>'

import multiprocessing
# from pprint import pprint

from simr.Configuration.Configuration import Configuration
from simr.Task.Runner import Runner


class Simr:
    config = None
    runner = None
    number_of_processors = 0

    def __init__(self):
        print("Simr v0.0.1")
        self.number_of_processors = multiprocessing.cpu_count()
        print("Processors found: {}".format(self.number_of_processors))

        # Parse console input
        self.config = Configuration('../config/simr.xml')

        # variables = self.config.get_variables()
        # print(variables)

        #tasks = self.config.get_tasks()
        #pprint(tasks)

        pass

    def run(self):
        """
        Loop through configuration to see which tasks need to be run
        """
        self.runner = Runner(self.number_of_processors)
        self.runner.add_tasks(self.config.get_tasks())
        self.runner.run()

        pass