import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
chess = []
idx_1 = [[0 for j in range(m)] for i in range(n)]
idx_2 = [[0 for j in range(m)] for i in range(n)]
ans = []
for _ in range(n):
    chess.append(sys.stdin.readline().rstrip())
'''
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
for k in range(n):
    for l in range(m):
        ck_line = []
        if k + 8 <= n and l + 8 <= m:
            for _ in range(k, k + 8):
                ck_line.append(sum(idx_1[k][l : l + 8]))
            ans.append(sum(ck_line))
'''
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
for k in range(n):
    for l in range(m):
        if k + 8 <= n and l + 8 <= m: 
            st_idx = idx_2[k][l]
            
        else: continue

print(*idx_2, sep= '\n')


