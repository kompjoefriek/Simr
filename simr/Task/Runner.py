import threading
import time
import datetime


"""
This file contains the class Runner, meant to run a given list of tasks
"""
__author__ = 'Sander Krause <sanderkrause@gmail.com>'
__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'


class Runner:
    tasks = []  # all tasks
    queue = []  # tasks in queue
    running_threads = []  # current running threads
    max_workers = 0

    def __init__(self, max_workers=2):
        self.tasks = []
        self.queue = []
        self.running_tasks = []
        self.max_workers = max_workers

    def add_tasks(self, tasks):
        self.tasks.extend(tasks)

    def start_next_task(self):
        if len(self.queue) > 0:
            task = self.queue.pop(0)
            print("Starting task: {}.".format(task.get_name()))
            thread = threading.Thread(target=self.run_in_thread, args=[task])
            thread.start()
            self.running_threads.append(thread)

    def on_task_finished(self, task, start_time):
        print("Finished task: {}. Time: {}".format(task.get_name(),
                                                   str(datetime.timedelta(seconds=time.time() - start_time))))
        self.start_next_task()

    def run_in_thread(self, task):
        start_time = time.time()
        try:
            task.run()
        finally:
            self.on_task_finished(task, start_time)

    def run(self):
        print("Found {} tasks, running max {} simultaneously.".format(len(self.tasks), self.max_workers))
        self.queue.extend(self.tasks)

        for _ in range(min(len(self.queue), self.max_workers - len(self.running_tasks))):
            self.start_next_task()
