#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Prints the metrics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """
    Parses a line and updates total_size and status_codes.
    """
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    except (IndexError, ValueError):
        pass

    return total_size, status_codes

if __name__ == "__main__":
    try:
        total_size = 0
        status_codes = {}
        line_count = 0

        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line, total_size, status_codes)

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)

