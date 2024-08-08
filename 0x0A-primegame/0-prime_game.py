#!/usr/bin/python3
"""module to solve prime game problem"""


def isWinner(x, nums):
    """return name of the player that won the most rounds"""
    if not nums or x < 1:
        return None
    n = max(nums)
    prime_nums = [True for _ in range(n + 1)]
    prime_nums[0] = prime_nums[1] = False
    p = 2
    while p * p <= n:
        if prime_nums[p]:
            for i in range(p * p, n + 1, p):
                prime_nums[i] = False
        p += 1
    c = 0
    for i in range(2, n + 1):
        if prime_nums[i]:
            c += 1
        prime_nums[i] = c
    player1 = 0
    player2 = 0
    for i in nums:
        if prime_nums[i] % 2 == 0:
            player2 += 1
        else:
            player1 += 1
    if player1 == player2:
        return None
    if player1 > player2:
        return "Maria"
    return "Ben"
