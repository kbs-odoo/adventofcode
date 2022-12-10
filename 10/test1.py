import sys
import re

noop_reg = re.compile("^noop")
add_reg = re.compile("^addx\s(.+)")
cycle = 0
tot = 1
matching_cycles = [{i: False} for i in range(20, 261, 40)]
plus = 0
print(matching_cycles)
last = 0
sig = 0
for i in sys.stdin.readlines():
    i = i.strip('\n')
    noop_match = noop_reg.search(i)
    add_match = add_reg.search(i)
    if noop_match:
        cycle += 1
        (key, value), = matching_cycles[plus].items()
        if not value and key == cycle:
            matching_cycles[plus][key] = key * tot
            sig += key * tot
            plus += 1
    elif add_match and add_match.group(1):
        for k in range(2):
            cycle+=1
            (key, value), = matching_cycles[plus].items()
            if not value and key == cycle:
                matching_cycles[plus][key] = key * tot
                sig += key * tot
                plus += 1
            if k == 1:
                tot += int(add_match.group(1))

print(matching_cycles)

print(sig)
