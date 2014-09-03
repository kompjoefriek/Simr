__author__ = 'Sander Krause <sanderkrause@gmail.com>'


from simr.Simr import Simr
from simr.Config import Config
from pprint import pprint


def main():
    # Parse console input
    config = Config('../config/simr.xml')
    tasks = config.get_tasks()
    pprint(tasks)

    # Use Simr to actually run tasks
    simr = Simr()

if __name__ == "__main__":
    main()