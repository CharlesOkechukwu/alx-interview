#!/usr/bin/python3
"""minimum operations calculation module"""


def minOperations(n):
    """Caluclate the amount of minimum operations required to reach n"""
    if n < 2:
        return 0
    if n % 2 == 0:
        div = 2
    else:
        div = 3

    prime_numbers = []
    while n > 1:
        if n % div == 0:
            prime_numbers.append(div)
            n = n // div
        else:
            div += 1
    return sum(prime_numbers)
