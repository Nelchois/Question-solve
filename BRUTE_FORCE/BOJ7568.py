import sys 
people = int(sys.stdin.readline())
status = []
ans = []
for i in range(people):
    weight, hight = map(int, sys.stdin.readline().rstrip().split(' '))
    status.append((weight, hight))
for j in range(people):
    ck_peo = status.pop(0)
    small = []
    middle = []
    big = []
    for k in range(people-1):
        w = status[k][0]
        h = status[k][1]
        if ck_peo[0] > w and ck_peo[1] > h:
            small.append(status[k])
        elif ck_peo[0] < w and ck_peo[1] < h:
            big.append(status[k])
        else:
            middle.append(status[k])
    ans.append(people-len(small)-len(middle))
    status.append(ck_peo)
print(*ans)


