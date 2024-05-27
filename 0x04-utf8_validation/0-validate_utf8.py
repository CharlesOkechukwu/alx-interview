#!/usr/bin/python3
"""module to validate if data is a valid utf-8"""


def validUTF8(data):
    """validate all data in a dataset to be correct utf-8 encoding
    return true if all data conatained are UTF-8"""
    bytes_left = 0
    for byte in data:
        if bytes_left > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_left -= 1
        else:
            if byte & 0b10000000 == 0:
                continue
            count = 0
            while byte & (0b10000000 >> count):
                count += 1
            if count < 2 or count > 4:
                return False
            bytes_left = count - 1
    return bytes_left == 0