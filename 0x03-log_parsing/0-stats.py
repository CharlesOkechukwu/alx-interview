#!/usr/bin/python3
"""module to parse logs from stdin"""
from sys import stdin


def print_logs():
    """parse logs from stdin"""
    stat_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    count = 0
    file_size = 0
    for line in stdin:
        count += 1
        try:
            data = line.split()
            file_size += int(data[-1])
            if data[-2] in stat_codes:
                stat_codes[data[-2]] += 1
        except Exception:
            pass
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for key, value in sorted(stat_codes.items()):
                if value:
                    print("{}: {}".format(key, value))