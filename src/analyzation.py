from collections import Counter
import pandas as pd

def aggregate_ips(events, out_path):
    """
    :param events: A dictionary that stores the ips and events parsed from the log file
    :param out_path: Where the created csv will be saved
    :return: None, simply creates a new csv file
    """
    # Uses the counter collection object to quickly create a count for each detection and the store it into a csv
    counts = Counter((event['ip'], event['event']) for event in events)
    data = [
        {'IP': ip, 'Event': event, 'Count': count}
        for (ip, event), count in counts.items()
    ]
    df = pd.DataFrame(data)
    df = df.sort_values(by="Count", ascending=False)
    df.to_csv(out_path, index=False)