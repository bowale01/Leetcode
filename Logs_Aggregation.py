Here’s a Python script that demonstrates how to aggregate system logs by parsing, filtering, and summarizing log data. This script reads log entries from a file, extracts relevant information, and aggregates it based on specific criteria, such as IP address or status code.

Python Script for Log Aggregation
1. Sample Log File Format:

Assuming we have a log file (/var/log/system.log) with the following format:
2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"


2.Python Script for Aggregating Logs:
import re
from collections import defaultdict
from typing import Dict, List, Tuple

# Define regex pattern to parse the log entries
log_pattern = re.compile(r'(?P<timestamp>\S+) (?P<level>\S+) (?P<ip>\S+) (?P<status>\d+) "(?P<message>.*)"')

def parse_log_line(line: str) -> Dict[str, str]:
    """Parse a log line into a dictionary."""
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return {}

def aggregate_logs(log_file_path: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    """Aggregate logs based on IP address and status code."""
    ip_aggregation = defaultdict(int)
    status_aggregation = defaultdict(int)

    with open(log_file_path, 'r') as file:
        for line in file:
            log_entry = parse_log_line(line)
            if log_entry:
                ip_aggregation[log_entry['ip']] += 1
                status_aggregation[log_entry['status']] += 1

    return ip_aggregation, status_aggregation

def print_aggregated_data(ip_aggregation: Dict[str, int], status_aggregation: Dict[str, int]):
    """Print the aggregated log data."""
    print("Aggregation by IP Address:")
    for ip, count in ip_aggregation.items():
        print(f"IP: {ip}, Count: {count}")

    print("\nAggregation by Status Code:")
    for status, count in status_aggregation.items():
        print(f"Status Code: {status}, Count: {count}")

if __name__ == "__main__":
    log_file_path = '/var/log/system.log'  # Path to the log file
    ip_aggregation, status_aggregation = aggregate_logs(log_file_path)
    print_aggregated_data(ip_aggregation, status_aggregation)


    Explanation:
Parsing Logs:

The parse_log_line function uses a regular expression to extract fields from each log entry.
The regex pattern captures timestamp, log level, IP address, status code, and the message.
Aggregating Logs:

The aggregate_logs function reads each line from the log file, parses it, and aggregates the count of occurrences based on IP address and status code.
defaultdict(int) is used to keep track of counts without needing to initialize dictionary keys manually.
Printing Results:

The print_aggregated_data function prints the aggregated results for IP addresses and status codes.
Running the Script
1.Save the script to a file, for example, aggregate_logs.py.

2. Ensure you have read access to the log file /var/log/system.log.

3.Run the script using Python:


python3 aggregate_logs.py
Additional Notes:
Customization: Modify the regex pattern and parsing logic if your log format differs.
Error Handling: Add error handling to manage issues such as file access errors or malformed log entries.
Performance: For very large log files, consider using more efficient methods like streaming or parallel processing.
This script provides a basic implementation for log aggregation. Depending on your needs, you may expand it to include more sophisticated filtering, aggregation by other criteria, or integration with log management systems.







