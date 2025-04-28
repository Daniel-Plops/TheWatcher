import re

def parse_logs(path):
    events = []
    # These are all the patterns the RegEx library looks for in the log file
    patterns = {
        'failed_login': r'Failed password.*from (\d+\.\d+\.\d+\.\d+)',
        'invalid_user': r'Invalid user (\w+)',
        'sudo_fail': r'sudo:.*authentication failure',
        'accepted_login': r'Accepted password for .* from (\d+\.\d+\.\d+\.\d+)',
        'ssh_disconnect': r'Connection closed by (\d+\.\d+\.\d+\.\d+)',
        'su_failed': r'su: .*incorrect password',
        'pam_failure': r'pam_unix\(sshd:auth\): authentication failure; .* rhost=(\d+\.\d+\.\d+\.\d+)'
    }

    # This just checks each line of the log file and if a detection is found, store it into the events dictionary
    with open(path, 'r') as f:
        for line in f:
            for event_type, pattern in patterns.items():
                match = re.search(pattern, line)
                if match:
                    ip = match.group(1) if match.groups() else "localhost"
                    events.append({
                        'ip': ip,
                        'event': event_type,
                        'raw': line.strip()
                    })
    return events