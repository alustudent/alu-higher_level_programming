#!/usr/bin/python3
"""Reads access log lines on stdin and prints size and status statistics."""
import sys

CODES = ("200", "301", "400", "401", "403", "404", "405", "500")


def print_stats(total_size, counts):
    """Prints the total file size and the count of each seen status code."""
    print("File size: {}".format(total_size))
    for code in CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


if __name__ == "__main__":
    total_size = 0
    counts = dict.fromkeys(CODES, 0)
    try:
        for n, line in enumerate(sys.stdin, 1):
            parts = line.split()
            # Malformed lines still count toward the 10-line cadence
            if len(parts) >= 2:
                if parts[-2] in counts:
                    counts[parts[-2]] += 1
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
            if n % 10 == 0:
                print_stats(total_size, counts)
        print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise
