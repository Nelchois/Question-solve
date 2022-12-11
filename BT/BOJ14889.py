import sys
n = int(sys.stdin.readline())
people = [i for i in range(1, n + 1)]
status = []
for st in range(n):
    status.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
team = []
score = []
board = []
ans = []
def make_team():
    if len(team) == n//2:
        for num_1 in team:
            for num_2 in team:
                if num_1 != num_2:
                    score.append(status[num_1 - 1][num_2 - 1])
                    if len(score) == (n//2)*(n//2 - 1) :
                        board.append(sum(score))
                        score.clear()
        return
    for i in people:
        if len(team) == 0:
            if i not in team:
                team.append(i)
                make_team()
                team.pop()
        elif len(team) != 0: 
            if i not in team and i > team[-1]:
                team.append(i)
                make_team()
                team.pop()

make_team()
for i in range(len(board)//2):
    dif = board.pop(0) - board.pop()
    if dif < 0:
        dif *= -1
    ans.append(dif)
print(min(ans))