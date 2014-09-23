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
    max_workers = 0
    interactive_mode = False
    config_file_name = ""

    def __init__(self):
        self.max_workers = multiprocessing.cpu_count()
        print("Processing units found: {}".format(self.max_workers))

    def set_max_workers(self, max_workers):
        self.max_workers = max_workers
        print("Max workers set to: {}".format(self.max_workers))

    def set_interactive_mode(self, interactive_mode):
        self.interactive_mode = interactive_mode
        if interactive_mode:
            print("Interactive mode: {} (not supported yet)".format(self.interactive_mode))

    def set_config_file_name(self, config_file_name):
        self.config_file_name = config_file_name
        print("Config file: {}".format(self.config_file_name))

    def run(self):
        # parse configuration
        self.config = Configuration(self.config_file_name)

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

        self.runner = Runner(self.max_workers)
        self.runner.add_tasks(self.config.get_tasks())
        self.runner.run()
