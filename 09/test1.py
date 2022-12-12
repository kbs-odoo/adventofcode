import sys
import re
import turtle
import numpy as np
head = turtle.Turtle()
head.color('yellow')
tail = turtle.Turtle()
tail.color('pink')
tail_poses = set()
pos_reg = re.compile("(.)\s(\d+)")

def check_tail(tail_position, head_position):
    head_x, head_y = head_position
    return tail_position not in [
        (head_x, head_y), (head_x, np.subtract(head_y, 1)), (head_x, np.add(head_y, 1)),
        (np.subtract(head_x, 1), np.subtract(head_y, 1)), (np.subtract(head_x, 1), np.add(head_y, 1)),
        (np.subtract(head_x, 1), head_y),
        (np.add(head_x, 1), np.subtract(head_y, 1)), (np.add(head_x, 1), np.add(head_y, 1)),
        (np.add(head_x, 1), head_y)
    ]

for i in sys.stdin.readlines():
    i = i.strip('\n')
    pos_match = pos_reg.search(i)
    dir = pos_match.group(1)
    val = pos_match.group(2)
    if dir == 'R':
        for _ in range(int(val)):
            head_x, head_y = head.pos()
            head_x = np.add(head_x, 1)
            head.setpos(head_x, head_y)
            tail_x, tail_y = tail.pos()
            # def check_tail(tail_position, head_position):
            if check_tail(tail.pos(), head.pos()):
                if np.add(tail_x, 2) == head_x and np.add(tail_y, 1) == head_y:
                    tail_x, tail_y = np.add(tail_x, 1), np.add(tail_y, 1)
                elif np.add(tail_x, 2) == head_x and np.subtract(tail_y, 1) == head_y:
                    tail_x, tail_y = np.add(tail_x, 1), np.subtract(tail_y, 1)
                else:
                    tail_x = np.add(tail_x, 1)
                tail.setpos(tail_x, tail_y)
                tail_poses.add((tail_x, tail_y))
                print((tail_x, tail_y))
    elif dir == 'U':
        for _ in range(int(val)):
            head_x, head_y = head.pos()
            head_y = np.add(head_y, 1)
            head.setpos(head_x, head_y)
            tail_x, tail_y = tail.pos()
            if check_tail(tail.pos(), head.pos()):
                if np.add(tail_x, 1) == head_x and np.add(tail_y, 2) == head_y:
                    tail_x, tail_y = np.add(tail_x, 1), np.add(tail_y, 1)
                elif np.subtract(tail_x, 1) == head_x and np.add(tail_y, 2) == head_y:
                    tail_x, tail_y = np.subtract(tail_x, 1), np.add(tail_y, 1)
                else:
                    tail_y = np.add(tail_y, 1)
                tail.setpos(tail_x, tail_y)
                tail_poses.add((tail_x, tail_y))
                print((tail_x, tail_y))
    elif dir == 'L':
        for _ in range(int(val)):
            head_x, head_y = head.pos()
            head_x = np.subtract(head_x, 1)
            head.setpos(head_x, head_y)
            tail_x, tail_y = tail.pos()
            if check_tail(tail.pos(), head.pos()):
                if np.subtract(tail_x, 2) == head_x and np.add(tail_y, 1) == head_y:
                    tail_x, tail_y = np.subtract(tail_x, 1), np.add(tail_y, 1)
                elif np.subtract(tail_x, 2) == head_x and np.subtract(tail_y, 1) == head_y:
                    tail_x, tail_y = np.subtract(tail_x, 1), np.subtract(tail_y, 1)
                else:
                    tail_x = np.subtract(tail_x, 1)
                tail.setpos(tail_x, tail_y)
                tail_poses.add((tail_x, tail_y))
                print((tail_x, tail_y))
    elif dir == 'D':
        for _ in range(int(val)):
            head_x, head_y = head.pos()
            head_y = np.subtract(head_y, 1)
            head.setpos(head_x, head_y)
            tail_x, tail_y = tail.pos()
            if check_tail(tail.pos(), head.pos()):
                if np.add(tail_x, 1) == head_x and np.subtract(tail_y, 2) == head_y:
                    tail_x, tail_y = np.add(tail_x, 1), np.subtract(tail_y, 1)
                elif np.subtract(tail_x, 1) == head_x and np.subtract(tail_y, 2) == head_y:
                    tail_x, tail_y = np.subtract(tail_x, 1), np.subtract(tail_y, 1)
                else:
                    tail_y = np.subtract(tail_y, 1)
                tail.setpos(tail_x, tail_y)
                tail_poses.add((tail_x, tail_y))
                print((tail_x, tail_y))

print(len(tail_poses))
