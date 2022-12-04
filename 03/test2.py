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
#print(priority)
#for i in sys.stdin.readlines():
#    i = i.strip('\n')
#    first, second = i[:len(i)//2], i[len(i)//2:]
#    intersect = set(Counter(first)).intersection(set(Counter(second)))
#    points += priority.get(next(iter(intersect)))
batches = []
appending_batch = []
count = 0
for i in sys.stdin.readlines():
    i = i.strip('\n')
    count+=1
    appending_batch.append(set(i))
    if count == 3:
        batches.append(appending_batch)
        appending_batch = []
        count = 0

badges = []
for i, j, k in batches:
    badges.append(i.intersection(j, k))

print(batches)
print(badges)
#print(points)
points = 0
for badge in badges:
    points += priority.get(next(iter(badge)))

print(points)
