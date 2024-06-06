#!/usr/bin/python3
"""
Can unlock all the boxes.
"""


def canUnlockAll(boxes):
    """
    Can unlock all the boxes.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
