import sys
import re

st = {"1": ["T", "P", "Z", "C", "S", "L", "Q", "N"], "2": ["L", "P", "T", "V", "H", "C", "G"],
      "3": ["D", "C", "Z", "F"], "4": ["G", "W", "T", "D", "L", "M", "V", "C"],
      "5": ["P", "W", "C"], "6": ["P", "F", "J", "D", "C", "T", "S", "Z"], "7": ["V", "W", "G", "B", "D"],
      "8": ["N", "J", "S", "Q", "H", "W"], "9": ["R", "C", "Q", "F", "S", "L", "V"]}

#st = {"1":["Z", "N"], "2":["M", "C", "D"], "3":["P"]}
for i in sys.stdin.readlines():
    p = re.compile("move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)")
    res = p.search(i.strip('\n'))
    print("1st group: ", res.group(1))
    print("2nd group: ", res.group(2))
    print("3rd group: ", res.group(3))
    el, out, into = int(res.group(1)), res.group(2), res.group(3)
#    import pdb
#    pdb.set_trace()
    st[res.group(3)].extend(st[res.group(2)][-int(res.group(1)):])
    for _ in range(int(res.group(1))):
        st[res.group(2)].pop()

#print(st)
stri = ""
for i in st:
    stri = stri+ st[i][-1]
print(stri)
