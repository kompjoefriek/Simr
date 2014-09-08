__author__ = 'Sander Krause <sanderkrause@gmail.com>'


from simr.Simr import Simr
from simr.Configuration.Configuration import Configuration
from pprint import pprint


def main():
    # Parse console input
    config = Configuration('../config/simr.xml')

    variables = config.get_variables()
    pprint(variables)

    tasks = config.get_tasks()
    pprint(tasks)

    # Use Simr to actually run tasks
    simr = Simr()

if __name__ == "__main__":
    main()