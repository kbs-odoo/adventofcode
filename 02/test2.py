import sys

select_points = {"X": 1, "Y": 2, "Z": 3}
win={"A": "Y", "B": "Z", "C": "X"}
draw={"A": "X", "B": "Y", "C": "Z"}
lose={"A": "Z", "B": "X", "C": "Y"}
points = 0
new_points = 0
for i in sys.stdin.readlines():
    opp, you = i.split(" ")
    print("OPP", opp)
    print("you", you)
    if you.strip('\n') == "Z":
        new_points+=6+select_points.get(win.get(opp.strip('\n')).strip('\n'))
    if you.strip('\n') == "Y":
        new_points+=3+select_points.get(draw.get(opp.strip('\n')).strip('\n'))
    if you.strip('\n') == "X":
        new_points+=select_points.get(lose.get(opp.strip('\n')).strip('\n'))

print(new_points)
