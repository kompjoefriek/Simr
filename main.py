__author__ = 'Sander Krause <sanderkrause@gmail.com>'

import argparse

from simr.Simr import Simr


def main():
    program_description = 'Simr v0.0.2'

    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('-m', dest='max_workers', type=int,
                        help='max workers allowed simultaneously (default: number of processing units)')
    parser.add_argument('-i', dest='interactive', action='store_true',
                        help='interactive mode (default: %(default)s)')
    parser.add_argument('configfile',
                        help='configuration file')

    # parse arguments and quit if something is missing
    args = parser.parse_args()

    print(program_description)

    # Use Simr to actually run tasks
    simr = Simr()
    if not args.max_workers is None:
        simr.set_max_workers(args.max_workers)
    if not args.interactive is None:
        simr.set_interactive_mode(args.interactive)
    if not args.configfile is None:
        simr.set_config_file_name(args.configfile)
    simr.run()

if __name__ == "__main__":
    main()