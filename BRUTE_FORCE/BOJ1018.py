import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
chess = []
idx_1 = [[0 for j in range(m)] for i in range(n)]
idx_2 = [[0 for j in range(m)] for i in range(n)]
ans = []
for _ in range(n):
    chess.append(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(m):
        if i%2 == 0:
            if j%2 == 0:
                if chess[i][j] == "B":
                    idx_1[i][j] = 0
                else:
                    idx_1[i][j] = 1
            else:
                if chess[i][j] == "W":
                        idx_1[i][j] = 0
                else:
                    idx_1[i][j] = 1
        else:
            if j%2 == 0:
                if chess[i][j] == "W":
                    idx_1[i][j] = 0
                else:
                    idx_1[i][j] = 1
            else:
                if chess[i][j] == "B":
                        idx_1[i][j] = 0
                else:
                    idx_1[i][j] = 1
for i in range(n):
    for j in range(m):
        if i%2 == 0:
            if j%2 == 0:
                if chess[i][j] == "W":
                    idx_2[i][j] = 0
                else:
                    idx_2[i][j] = 1
            else:
                if chess[i][j] == "B":
                        idx_2[i][j] = 0
                else:
                    idx_2[i][j] = 1
        else:
            if j%2 == 0:
                if chess[i][j] == "B":
                    idx_2[i][j] = 0
                else:
                    idx_2[i][j] = 1
            else:
                if chess[i][j] == "W":
                        idx_2[i][j] = 0
                else:
                    idx_2[i][j] = 1

for line in range(n):
    for row in range(m):
        field_sum_2 = []
        if line + 8 <= n and row + 8 <= m:
            for c in range(line, line + 8):
                a = sum(idx_2[c][row: row + 8])
                field_sum_2.append(a)
            ans.append(sum(field_sum_2))
for line in range(n):
    for row in range(m):
        field_sum_1 = []
        if line + 8 <= n and row + 8 <= m:
            for c in range(line, line + 8):
                a = sum(idx_1[c][row: row + 8])
                field_sum_1.append(a)
            ans.append(sum(field_sum_1))
print(min(ans))



