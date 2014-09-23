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
    curses_screen = None

    def __init__(self):
        self.max_workers = multiprocessing.cpu_count()
        print("Processing units found: {}".format(self.max_workers))

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

        if self.interactive_mode:
            import curses  # http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

            # init curses
            self.curses_screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.curses_screen.keypad(1)

            # draw screen
            self.curses_screen.addstr(0, 0, "Current mode: Typing mode")
            self.curses_screen.refresh()

            while 1:
                c = self.curses_screen.getch()
                if c == ord('p'):
                    # PrintDocument()
                    pass
                elif c == ord('q'):
                    break  # Exit the while()
                elif c == curses.KEY_HOME:
                    # x = y = 0
                    pass

            self.quit()
            exit()
            pass

        self.runner = Runner(self.max_workers)
        self.runner.add_tasks(self.config.get_tasks())
        self.runner.run()

    def quit(self):
        if self.interactive_mode:
            import curses

            # destroy curses
            self.curses_screen.keypad(0);
            curses.nocbreak();
            curses.echo()
            curses.endwin()