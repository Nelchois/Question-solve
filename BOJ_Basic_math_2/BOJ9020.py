import sys
case = int(sys.stdin.readline())
num_bol = [True]*10001
for n in range(2, 101):
    if num_bol[n] == True:
        for m in range(n+n, 10001, n):
            num_bol[m] = False
for i in range(case):
    ck_num = int(sys.stdin.readline())
    count = 0
    find_list = []
    min_list = []
    ans = []
    m = int(ck_num/2)
    for i in range(m):
        if (num_bol[m - i] == True) and (num_bol[m + i] == True):
            print(m-i, m+i)
            break
