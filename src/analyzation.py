# Use the logs collected by log_parser to generate a useful json file that will be used in
# the visualizer.py file
from collections import Counter
import pandas as pd

def aggregate_ips(ip_list, out_path="data/attacks.csv"):
    count = Counter(ip_list)
    df = pd.DataFrame(count.items(), columns=["IP", "Attempts"])
    df = df.sort_values(by="Attempts", ascending=False)
    df.to_csv(out_path, index=False)