__author__ = 'Sander Krause <sanderkrause@gmail.com>'

import os
import multiprocessing

import psutil



# from pprint import pprint
from simr.Configuration.Configuration import Configuration
from simr.Task.Runner import Runner


class Simr:
    program_description = 'Simr v0.0.2'
    config = None
    runner = None
    processing_units = 0
    max_workers = 0
    interactive_mode = False
    config_file_name = ""
    curses_screen = None

    def __init__(self):
        self.processing_units = multiprocessing.cpu_count()
        print("Processing units found: {}".format(self.processing_units))
        self.max_workers = self.processing_units

    def set_max_workers(self, max_workers):
        self.max_workers = max_workers
        print("Max workers set to: {}".format(self.max_workers))

    def set_interactive_mode(self, interactive_mode):
        self.interactive_mode = interactive_mode
        if interactive_mode:
            print("Interactive mode: {}".format(self.interactive_mode))

    def set_config_file_name(self, config_file_name):
        self.config_file_name = config_file_name
        print("Config file: {}".format(self.config_file_name))

    def interactive_screen(self, win):
        import curses

        self.curses_screen = win

        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        self.curses_screen.keypad(1)
        self.curses_screen.nodelay(1)
        self.curses_screen.timeout(1000)

        counter = 1

        # draw screen
        self.curses_screen.box()
        self.curses_screen.addstr(0, 1, " {} ".format(Simr.program_description))
        self.curses_screen.addstr(4, 1, "Press up, down, or q")

        y, x = self.curses_screen.getmaxyx()
        self.curses_screen.hline(2, 1, curses.ACS_HLINE, x - 2)

        # flush any input
        curses.flushinp()

        while 1:
            self.curses_screen.addstr(1, 1, "Max workers: {}".format(self.max_workers))
            self.curses_screen.addstr(3, 1, "Counter: {}".format(counter))
            self.curses_screen.refresh()

            c = self.curses_screen.getch()
            if c == ord('q'):
                self.curses_screen.clear()
                return 0
            elif c == curses.KEY_UP:
                self.max_workers += 1
                if self.max_workers > self.processing_units:
                    self.max_workers = self.processing_units
            elif c == curses.KEY_DOWN:
                self.max_workers -= 1
                if self.max_workers < 0:
                    self.max_workers = 0
                pass

            counter += 1

    def run(self):
        try:
            # parse configuration
            self.config = Configuration(self.config_file_name)
        except FileNotFoundError as e:
            print("[Error] File not found: {}".format(e.filename))
            exit(1)

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

        if self.interactive_mode:
            import curses  # http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

            curses.wrapper(self.interactive_screen)
        else:
            self.runner.run()
