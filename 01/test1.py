import sys

a = []
outputs = []
max_sum = 0
sums = []
for i in sys.stdin.readlines():
    if i =="\n":
        outputs.append(a)
        a = []
    else:
        a.append(int(i))

for j in outputs:
    if max_sum < sum(j):
        max_sum = sum(j)

for j in outputs:
    sums.append(sum(j))

sums.sort(reverse=True)
print(outputs)
print(max_sum)
print(sums[0])
