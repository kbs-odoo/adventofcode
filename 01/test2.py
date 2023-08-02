import sys

a = []
outputs = []
for i in sys.stdin.readlines():
    if i =="\n":
        outputs.append(a)
        a = []
    else:
        a.append(int(i))

summer=[]
for k in outputs:
    summer.append(sum(k))

summer.sort(reverse=True)
print(summer[:3])
print(sum(summer[:3]))
print("HELLO")
