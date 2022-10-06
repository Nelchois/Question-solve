import sys
from collections import deque
house = int(sys.stdin.readline())
cost = []
color = 0
R = deque()
G = deque()
B = deque()
route = {}
for i in range(house):
    r, g, b = map(int, sys.stdin.readline().rstrip().split(' '))
    R.append(r)
    G.append(g)
    B.append(b)
def in_color():
    for _ in range(house):
        r1 = R.popleft()
        r2 = R.popleft()
        g1 = G.popleft()
        g2 = G.popleft()
        b1 = B.popleft()
        b2 = B.popleft()
        route['12'] = r1 + g2
        route['13'] = r1 + b2
        route[]
