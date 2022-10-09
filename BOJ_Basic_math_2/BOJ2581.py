import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(m, n+1) if m <= i <= n]
ans = []
for i in len(num_list):
    ck = num_list.pop()
    if ck == 2 or 3 or 5 or 7:
        ans.append(ck)
    else:
    if len(ans) == 0:
        print(-1)
    else:
        print(sum(ans))
        print(min(ans))

     
