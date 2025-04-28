import argparse
import pandas as pd
import sys

from src.visualizer import show
from src.log_parser import parse_logs
from src.analyzation import aggregate_ips


def main():
    # This whole section deals with the CLI elements and flags
    parser = argparse.ArgumentParser(description=("╭───────────────────────────────────────────────────────────────────────────────╮\n"
                                                  "                                 The Watcher                                   \n"
                                                  "                             Built by Daniel Lopez                             \n"),
                                     epilog=(
                                         "\n"
                                         "  Thank you for using The Watcher.\n"
                                         "  Stay vigilant.\n"
                                         "╰───────────────────────────────────────────────────────────────────────────────╯\n"
                                     ),
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )

    parser.add_argument('-l', '--log', type=str, metavar='log',required=True,
                        help='Path to the log file to analyze')
    parser.add_argument('-o', '--out', type=str, metavar='output', default='data/attacks.csv',
                        help='Path to save the output CSV (default: data/attacks.csv)')
    parser.add_argument('-t', '--top', type=int, metavar='top',default=10,
                        help='Number of top IPs to visualize (default: 10)')
    parser.add_argument('--bar', action='store_true', default=True,
                        help='Visualize the bar graph (default: True)')
    parser.add_argument('--table', action='store_true',
                        help='Visualize the attack table (default: False)')

    # If no commands are inputted, don't try to parse incorrectly and show help page
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Parses logs
    detections = parse_logs(args.log)

    # Creates csv file based on detections
    aggregate_ips(detections, args.out)

    # Uses created csv to display info
    df = pd.read_csv(args.out)
    data = df.to_dict('records')

    show(data, args.top, args.table)


if __name__ == '__main__':
    main()