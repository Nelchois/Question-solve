import sys

num = int(sys.stdin.readline())
idx_list = [0]*num
ans = []
def n_queens (i, col):
    n = len(col) -1
    if (promising(i, col)):
        if (i == n):
            ans.append(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising (i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag 

col = [0] * (num + 1)
n_queens(1, col)
print(len(ans))