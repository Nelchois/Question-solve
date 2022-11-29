import sys
from itertools import combinations
n = int(sys.stdin.readline())
people = [i for i in range(n)]
status = []
for st in range(n):
    status.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
team = []
board = []
def make_team():
    for set in combinations(people, 3):
        left = list(set)
        right = [i for i in people if i not in left]
        team.append(left)
        team.append(right)
    return
def cal():
    for idx in range(len(team)):
        if idx%2 == 0:
            for i in combinations(team[idx], 2):
                q = list(i)
                board.append(status[q[0]][q[1]])
        if idx%2 != 0:        
            for i in combinations(team[idx], 2):
                q = list(i)
                board.append(status[q[0]][q[1]])
            
make_team()
print(team)