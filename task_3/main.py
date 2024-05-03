from pathlib import Path
import sys


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

def main():
    dir = sys.argv[1]
    file_path = Path(dir)
    list = load_logs(file_path)
    print(list)

if __name__ == "__main__":
    main()