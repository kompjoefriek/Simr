__author__ = 'Sander Krause <sanderkrause@gmail.com>'

import os
import multiprocessing

import psutil

# from pprint import pprint

from simr.Configuration.Configuration import Configuration
from simr.Task.Runner import Runner


class Simr:
    config = None
    runner = None
    number_of_processors = 0

    def __init__(self):
        self.number_of_processors = multiprocessing.cpu_count()
        print("Processing units found: {}".format(self.number_of_processors))

        # parse configuration
        self.config = Configuration('../config/simr.xml')

        #variables = self.config.get_variables()
        #pprint(variables)

        #tasks = self.config.get_tasks()
        #pprint(tasks)

        # change to low priority
        process = psutil.Process()
        if os.name is "nt":
            process.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        else:
            process.nice(10)  # should about be the same as BELOW_NORMAL_PRIORITY_CLASS

    def run(self):
        """
        Loop through configuration to see which tasks need to be run
        """
        self.runner = Runner(self.number_of_processors)
        self.runner.add_tasks(self.config.get_tasks())
        self.runner.run()
