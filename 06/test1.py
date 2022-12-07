import sys
stri = ""
for i in sys.stdin.readlines():
    count = 0
    for j in i:
        count += 1
#        import pdb
#        pdb.set_trace()
        for k in i[count-1:count+3]:
            if k not in stri:
                stri += k
        if len(stri) == 4:
            count+=3
            break
        else:
            stri = ""

print(count)
