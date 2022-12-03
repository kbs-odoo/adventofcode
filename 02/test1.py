import sys

select_points = {"X": 1, "Y": 2, "Z": 3}
win={"A": "Y", "B": "Z", "C": "X"}
draw={"A": "X", "B": "Y", "C": "Z"}
lose={"A": "Z", "B": "X", "C": "Y"}

points = 0
for i in sys.stdin.readlines():
    opp, you = i.split(" ")
    print("OPP", opp)
    print("you", you)
    if win.get(opp) == you.strip('\n'):
        points+=6+select_points.get(you.strip('\n'))
    if draw.get(opp) == you.strip('\n'):
        points+=3+select_points.get(you.strip('\n'))
    if lose.get(opp) == you.strip('\n'):
        points+=select_points.get(you.strip('\n'))

print(points)
