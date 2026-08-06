from datetime import datetime
from collections import Counter
from colorama import Fore, Style, init

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
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))
    
