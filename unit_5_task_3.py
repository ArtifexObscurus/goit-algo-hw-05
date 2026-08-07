from datetime import datetime
from collections import Counter
from colorama import Fore, Style, init
import sys

# Initialize colorama for cross-platform output.
init(autoreset=True)

def parse_log_line(line: str) -> dict[str, str]:
    """
    Parse a log line into its components.

    Parameters
    ----------
    line : str
        A single line from the log file.

    Returns
    -------
    dict[str, str]
        A dictionary containing date, time, log level and message.    
    """    
    date, time, level, message = line.strip().split(maxsplit=3)    

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }
    
def load_logs(file_path: str) -> list[dict[str, str]]:
    """
    Read logs from file.

    Parameters
    ----------
    file_path : str
        String with path to the log file.

    Returns
    -------
    list[dict[str, str]]
        A list of dictionaries containing parsed log records.
    """
    logs: list[dict[str, str]] = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    logs.append(parse_log_line(line))
                except ValueError:
                    print("Error: Invalid log format. Unable to parse log file.")
                    return []     
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return []

    except OSError as error:
        print(f"Error: {error}")
        return []

    return logs

def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    """
    Filter list with logs by chosen level.

    Parameters
    ----------
    logs : list[dict[str, str]]
        A list of dictionaries containing parsed log records.
    level : str
        The log level to filter by.

    Returns
    -------
    list[dict[str, str]]
        A list of log records matching the specified log level.
    """
    level = level.upper()
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    """
    Count the number of log records for each log level.

    Parameters
    ----------
    logs : list[dict[str, str]]
        A list of dictionaries containing parsed log records.
    
    Returns
    -------
    dict[str, int]
        A dictionary with the number of log records for each level.
    """
    return dict(Counter(log["level"] for log in logs))
    
def display_log_counts(counts: dict[str, int]) -> None:
    """
    Display log count in a formatted table

    Parameters
    ----------
    counts : dict[str, int]
        A dictionary containing the number of log records for each level.
    """
    header_level = "Log level"
    header_count = "Count"

    # Determine the width of the first column based on the header and log levels.
    level_width = max(len(header_level), *(len(level) for level in counts))

    lines = [
        f"{header_level:<{level_width}} | {header_count}",
        f"{'-' * level_width}-|-{'-' * len(header_count)}",
    ]

    colors = {
        "ERROR": Fore.RED,
        "INFO": Fore.BLUE,
        "WARNING": Fore.YELLOW,
    }

    for level, count in counts.items():
        color = colors.get(level, "")
        lines.append(f"{color}{level:<{level_width}} | {count}{Style.RESET_ALL}")

    print("\n".join(lines))

def main() -> None:
    """Run the log analysis program."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file> [log_level]")
        return

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nLogs details for level '{level.upper()}':")

        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log["message"]}")

if __name__ == "__main__":
    main()