import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(m, n+1) if m <= i <= n]
ans = []
for i in (num_list):
    ck = [2, 3, 5, 7]
    if i <= 7:
        if i in ck:
            ans.append(i)    
    else:
        for j in range(4):
            if i%ck[j] == 0:
                break
            elif i%ck[j] != 0 and j == 3:
                ans.append(i)
if len(ans) == 0:
        print(-1)
else:
    if ans[0]**2 > ans[-1]:
        print(sum(ans))
        print(min(ans))

    elif ans[0]**2 < ans[-1]:
        for i in range(len(ans)):
            try:
                ans.remove(ans[i]**2)
            except:
                continue
        print(sum(ans))
        print(min(ans))
