__author__ = 'Sander Krause <sanderkrause@gmail.com>'

import concurrent.futures


class Runner:

    pool = []
    number_of_workers = 2

    def __init__(self, max_workers=2):
        self.pool = []
        self.number_of_workers = max_workers

    def next_task(self):
        return self.pool.pop()

    def run(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.number_of_workers) as executor:
            # TODO: replace this with actual code
            executor.submit(self.next_task())