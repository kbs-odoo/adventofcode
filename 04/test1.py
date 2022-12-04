import sys

tot = 0
for i in sys.stdin.readlines():
    pair = i.strip("\n").split(",")
    print(pair)
    i, j = pair[0].split("-"), pair[1].split("-")
    first, second = {k for k in range(int(i[0]), int(i[-1]) + 1)}, {m for m in range(int(j[0]), int(j[-1]) + 1)}
    val = second >= first or first >= second
    if val:
        tot += 1

print(tot)
