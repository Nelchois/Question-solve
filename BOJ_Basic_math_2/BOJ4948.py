import sys
while True:
    num = int(sys.stdin.readline().rstrip())
    case = 2 * num
    if case == 0:
        break
    bol_list = [True]*(case+1)
    for i in range(2, int(case ** 0.5) + 1):
        if bol_list[i] == True:
            for j in range(i+i, case + 1, i):
                bol_list[j] = False
    ans = [n for n in range(num+1, case+1) if bol_list[n] == True]
    if ans[0] == 1:
        ans.pop(0)
    print(len(ans))
