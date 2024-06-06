#/usr/bin/python3
"""
Can unlock all the boxes.
"""

def canUnlockAll(boxes):
  """
  Can unlock all the boxes.
  """
  if len(boxes) == 0:
    return False
  if len(boxes[0]) == 0:
    return False
  if len(boxes) == 1:
    return True
  if len(boxes[0]) == 1:
    return True
  for i in range(len(boxes)):
    for j in range(len(boxes[0])):
      if boxes[i][j] == 1:
        for k in range(len(boxes[0])):
          if boxes[i][k] == 1:
            boxes[i][k] = 0
  for i in range(len(boxes)):
    for j in range(len(boxes[0])):
      if boxes[i][j] == 1:
        return False
  return True
