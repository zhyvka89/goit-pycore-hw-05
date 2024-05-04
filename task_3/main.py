import sys
from pathlib import Path
from typing import Counter


def parse_log_line(line: str) -> dict:
    date, time, log, *args = line.split()
    msg = ' '.join(args)
    return {'date': date, 'time': time, 'log': log, 'message': msg }


def load_logs(file_path: str) -> list:
    if file_path.exists():
        try:
            with open(file_path) as file:
                list_of_logs = list()
                lines = [el.strip() for el in file.readlines()]
                for line in lines:
                    res = parse_log_line(line)
                    list_of_logs.append(res)
                return list_of_logs
        except:
            print("Oops, error!")
    else:
        print("File does not exist.")


def filter_logs_by_level(logs: list, level: str) -> list:
    filter_logs = filter(lambda x: x['log'].lower() == level, logs)
    filtered_logs_list = list(filter_logs)
    return list(filtered_logs_list)


def count_logs_by_level(logs: list) -> dict:
    list_of_levels = list()
    for log in logs:
        for key, value in log.items():
            if key == "log":
                list_of_levels.append(value)
    logs_count = Counter(list_of_levels)
    return logs_count


def display_log_counts(counts: dict):
    print(f'{'Log Level':<10} {'|':>5} {'Quantity':>15}')
    print('--------------------------------------')
    for key, value in counts.items():
        print(f'{key:<10} {'|':>5} {value:>10}')
        

def main():
    dir = sys.argv[1]
    file_path = Path(dir)
    list = load_logs(file_path)
    counts = count_logs_by_level(list)
    display_log_counts(counts)
    if len(sys.argv) > 2:
        log_level = sys.argv[2]
        print(f"Details for log level '{log_level.upper()}'")
        filtered_logs = filter_logs_by_level(list, log_level)
        for log in filtered_logs:
            print(f'{log['date']} {log['time']} - {log['message']}')

if __name__ == "__main__":
    main()