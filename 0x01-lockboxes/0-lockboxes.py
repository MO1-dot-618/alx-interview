#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    function that tells if all boxes are unlocked
    boxes can be opened with keys inside other boxes
    """
    n = len(boxes)
    unlocked = [0,] * n
    unlocked[0] = 1
    for i in range(n):
        if unlocked[i] == 1:
            for key in boxes[i]:
                unlocked[key] = 1
    for i in range(n):
        if unlocked[i] == 1:
            for key in boxes[i]:
                unlocked[key] = 1
    return unlocked == [1,] * n
