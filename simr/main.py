__author__ = 'Sander Krause <sanderkrause@gmail.com>'

from simr.Simr import Simr


def main():
    print("Simr v0.0.1")

    # Use Simr to actually run tasks
    simr = Simr()
    simr.run()


if __name__ == "__main__":
    main()