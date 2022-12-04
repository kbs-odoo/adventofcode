import sys
from collections import Counter
from string import ascii_lowercase as low
from string import ascii_uppercase as high

points =0
priority={}
for i, j in zip(low, range(1, 27)):
    priority[i] = j
for i, j in zip(high, range(27, 53)):
    priority[i] = j
print(priority)
for i in sys.stdin.readlines():
    i = i.strip('\n')
    first, second = i[:len(i)//2], i[len(i)//2:]
    intersect = set(Counter(first)).intersection(set(Counter(second)))
    points += priority.get(next(iter(intersect)))


print(points)
