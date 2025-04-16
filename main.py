import src.analyzation
import src.visualizer
import src.log_parser
import argparse

def main():
    parser = argparse.ArgumentParser(description="--------------------------\n"
                                                 "            The           \n"
                                                 "          Watcher         \n"
                                                 "--------------------------\n"
                                                 "     Built by Daniel Lopez")

    parser.add_argument('-l', '--log', type=str, required=True,
                        help='Path to the log file to analyze')
    parser.add_argument('-o', '--out', type=str, default='data/attacks.csv',
                        help='Path to save the output CSV (default: data/attacks.csv)')
    parser.add_argument('-t', '--top', type=int, default=10,
                        help='Number of top IPs to visualize (default: 10)')
    parser.add_argument('-s', '--show', action='store_true',
                        help='Whether to display a plot of the results')

    args = parser.parse_args()

    # Run functions / other programs for other functionality
    pass

if __name__ == '__main__':
    main()