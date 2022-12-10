import sys
import re

noop_reg = re.compile("^noop")
add_reg = re.compile("^addx\s(.+)")
cycle = 0
matching_cycles = [{i: False} for i in range(20, 261, 40)]
matching_nums = [i for i in range(0, 241, 40)]
print(matching_cycles)
init_pos = 1
pos = [init_pos,init_pos+1,init_pos+2]
sig = 0
for i in sys.stdin.readlines():
    i = i.strip('\n')
    noop_match = noop_reg.search(i)
    add_match = add_reg.search(i)
#    import pdb
#    pdb.set_trace()
    if noop_match:
        cycle += 1
        if cycle in pos:
            print("#", end="")
        else:
            print(".", end="")
        if cycle in matching_nums:
            print("", end="\n")
            cycle = 0
    elif add_match and add_match.group(1):
        for k in range(2):
            cycle += 1
            if cycle in pos:
                print("#", end="")
            else:
                print(".", end="")
            if cycle in matching_nums:
                print("", end="\n")
                cycle = 0
#            if k == 1:
#                init_pos += int(add_match.group(1))
#                pos = [init_pos,init_pos+1,init_pos+2]
        init_pos += int(add_match.group(1))
        pos = [init_pos,init_pos+1,init_pos+2]


#print(matching_cycles)

#print(sig)

