import sys
m, n = map(int, sys.stdin.readline().rstrip().split(' '))
num_list = [True]*(n)
for i in range(2, int(n ** 0.5) + 1):
    if num_list[i] == True:
        for j in range(i+i, n, i):
            num_list[j] = False
ans = [i for i in range(2, n) if num_list[i] == True]

if m <= 2:
    print(*ans, sep= '\n')
elif m > 2:
    for i in range(len(ans)):
        if ans[i] >= m:
            idx = i
            break
    print(*ans[idx:: ], sep= '\n')




