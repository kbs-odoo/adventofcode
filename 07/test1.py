import re
import sys

cd_reg = re.compile("^\$\scd\s(.*)?")
dir_reg = re.compile("dir (.*)?")
file_reg = re.compile("(\d+)\s\S+")
back_path_reg = re.compile("([a-zA-Z]*\/$)")
path = "/"
new_dir = ""
map_tree = {}
for i in sys.stdin.readlines():
    cd_match = cd_reg.search(i)
    dir_match = dir_reg.search(i)
    file_match = file_reg.search(i)
    if cd_match and cd_match.group(1) != '..' and cd_match.group(1):
        if cd_match.group(1) != "/":
            path += cd_match.group(1) + "/"
        map_tree[path] = map_tree.get(path, 0)
    if cd_match and cd_match.group(1) == '..' and cd_match.group(1) :
        back_path_match = back_path_reg.search(path)
        path = path[:len(path)-len(back_path_match.group(1))]
    if dir_match and dir_match.group(1):
        new_dir = path + dir_match.group(1) + "/"
        map_tree[new_dir] = 0
    if file_match and file_match.group(1):
        map_tree[path] += int(file_match.group(1))

new_sum = {}
summation={}
for i in map_tree:
    summation[i] = map_tree.get(i)
    for j in map_tree:
        if i.strip(' \n')!=j.strip(' \n') and re.compile("^{}".format(i.strip(' \n'))).search(j.strip(' \n')):
            summation[i]+=map_tree[j]
# print(summation)
new_sum = 0
for i in summation.values():
    if i<=100000:
        new_sum+=i

# for i, j in zip(summation.keys(), summation.values()):
#     print(i, " : ", j)
print("Sum of under 100000 dirs:", new_sum)
