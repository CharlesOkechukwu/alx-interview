#!/usr/bin/python3
"""making change from a list of coin module"""


def makeChange(coins, total):
    """return the fewest number of coins needed
    to meet a given amount total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    min_op = 0
    for coin in coins:
        if total <= 0:
            break
        min_op += total // coin
        total = total % coin
    if total != 0:
        return -1
    return min_op
