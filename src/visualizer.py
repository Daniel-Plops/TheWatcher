from rich.console import Console
from rich.table import Table
from rich.text import Text

def display_table(data, top_n):
    """
    :param data: Dictionary of important detection data
    :param top_n: Determines the max number of detections shown
    :return: None, prints out a table with the detections requested
    """
    console = Console()
    console.print("╭────────────────────────────────────────╮")
    console.print("       [bold underline]Table of Top Attack Attempts[/bold underline]")

    data = sorted(data, key=lambda x: x['Count'], reverse=True)[:top_n]

    # Creates the rich table object that formats all the info in a human readable way
    table = Table(show_header=True, header_style="#EE8EAE")

    table.add_column("IP", style="cyan")
    table.add_column("Event Type", style="#ffdc2b")
    table.add_column("Count", justify="right", style="green")

    for row in data:
        table.add_row(row['IP'], row['Event'], str(row['Count']))

    console.print(table)
    console.print("╰────────────────────────────────────────╯")

def display_bar(data, top_n):
    """
        :param data: Dictionary of important detection data
        :param top_n: Determines the max number of detections shown
        :return: None, prints out a bar chart with the detections requested
        """
    console = Console()

    console.print("╭──────────────────────────────────────────────────╮")
    console.print("             [bold underline]Chart of Top Attack Attempts[/bold underline]\n")

    data = sorted(data, key=lambda x: x['Count'], reverse=True)[:top_n]

    max_occ = max(row['Count'] for row in data)

    # Creates the bar chart line by line for each type of detection
    for row in data:
        ip = row['IP']
        count = row['Count']

        # Do some color-coding based on number of occurrences detected
        if count == max_occ:
            color = "red"
        elif count >= max_occ/2:
            color = "yellow"
        else:
            color = "green"

        bar = "█" * int((count / max_occ) * 30)

        # Use the rich Text object to make everything colored and correctly formatted
        color_bar = Text(str(bar), style=color)
        line = Text.assemble(
            (f" {ip:<16}", "cyan"),
            color_bar,
            (f" {count}", color)
        )
        console.print(line)
    console.print("╰──────────────────────────────────────────────────╯")

def show(attack_data, top_n, show_table):
    # Simple way to decide which display to show the user
    if show_table:
        display_table(attack_data, top_n)
    else:
        display_bar(attack_data, top_n)