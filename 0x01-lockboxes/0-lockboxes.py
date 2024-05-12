#!/usr/bin/python3
"""module to unlock boxes in a list using keys in another list"""


def canUnlockAll(boxes):
    """method to check if all keys can open all boxes and if all
    boxes can be opened"""
    if not boxes or len(boxes) == 0:
        return False
    box_keys = []
    locked = []
    for i in range(len(boxes)):
        if i > 0 and i not in box_keys:
            locked.append(i)
        else:
            box = boxes[i]
            if len(box) > 0:
                for key in box:
                    if key < len(boxes) and key not in box_keys:
                        box_keys.append(key)
                    elif key >= len(boxes):
                        return False
    if len(locked) > 0:
        lock_cpy = [i for i in locked]
        for index, value in enumerate(lock_cpy):
            if value in box_keys:
                box = boxes[value]
                for key in box:
                    if key < len(boxes) and key not in box_keys:
                        box_keys.append(key)
                    elif key >= len(boxes):
                        return False
                locked.remove(value)
        if len(locked) > 0:
            return False
    return True
