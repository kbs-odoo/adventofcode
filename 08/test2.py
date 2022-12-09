import sys

count=0
tree =0
map_tree = {}
map_tree_cols = {}
for i in sys.stdin.readlines():
    count+=1
    print(i)
    a = i.strip('\n')
    map_tree[count] = [int(i) for i in a]

count_col = 0
tot = 0
for col in map_tree.values():
    for j in col:
        count_col+= 1
        if count_col == count+1:
            count_col = 1
        if map_tree_cols.get(count_col, []):
            map_tree_cols[count_col] = map_tree_cols[count_col]+[j]
        else:
            map_tree_cols[count_col] = [j]

tree = count*4 -4

print("ROWS:" ,map_tree)

for i in map_tree.keys():
    if i==1 or i==5:
        continue
    for j in range(1, len(map_tree[i][1:len(map_tree[i])-1])):
        if max(map_tree[i][j+1:len(map_tree[i])])< map_tree[i][j]:
            print(map_tree[i-1])

print("COLS", map_tree_cols)

inn_tree = 0
for i in range(2, count):
    print(map_tree[i])
    for j in range(2, count):
        print("ROW:", i, "COL", j, map_tree[i][:j-1], map_tree[i][j-1], map_tree[i][j:count+1])
        print("NEXT LOGIC", map_tree_cols[j][:i-1],map_tree[i][j-1], map_tree_cols[j][i:count+1])
        if map_tree[i][j-1]>max(map_tree[i][:j-1]) or map_tree[i][j-1]>max(map_tree[i][j:count+1]) or map_tree[i][j-1]>max(map_tree_cols[j][:i-1]) or  map_tree[i][j-1] > max(map_tree_cols[j][i:count+1]):
            inn_tree +=1

print(inn_tree)
print(inn_tree+tree)
top_score = 1
count_1 = 0
topping = 1
for i in range(2, count):
    print(map_tree[i])
    for j in range(2, count):
        print("ROW:", i, "COL", j, map_tree[i][:j-1], map_tree[i][j-1], map_tree[i][j:count+1])
        print("NEXT LOGIC", map_tree_cols[j][:i-1],map_tree[i][j-1], map_tree_cols[j][i:count+1])
        for top in map_tree[i][:j-1][::-1]:
            if map_tree[i][j-1]>top:
                count_1+=1
            if map_tree[i][j-1]==top:
                count_1+=1
                break
            if map_tree[i][j-1]<top:
                count_1+=1
                break
        top_score*=count_1
        count_1 = 0
        for top in map_tree[i][j:count+1]:
            if map_tree[i][j-1]>top:
                count_1+=1
            if map_tree[i][j-1]==top:
                count_1+=1
                break
            if map_tree[i][j-1]<top:
                count_1+=1
                break
        top_score*=count_1
        count_1 = 0
        for top in map_tree_cols[j][:i-1][::-1]:
            if map_tree[i][j-1]>top:
                count_1+=1
            if map_tree[i][j-1]==top:
                count_1+=1
                break
            if map_tree[i][j-1]<top:
                count_1+=1
                break
        top_score*=count_1
        count_1 = 0
        for top in map_tree_cols[j][i:count+1]:
            if map_tree[i][j-1]>top:
                count_1+=1
                continue
            if map_tree[i][j-1]==top:
                count_1+=1
                break
            if map_tree[i][j-1]<top:
                count_1+=1
                break
        top_score*=count_1
        count_1 = 0
        if topping<top_score:
            topping = top_score
        top_score = 1
print(topping)
