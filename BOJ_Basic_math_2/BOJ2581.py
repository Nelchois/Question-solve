import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(m, n+1)]
prime_list = []
ans = []
for i in num_list:
    if i == 2:
        ans.append(i)
    elif i == 3:
        ans.append(i)
    for j in range(2, i//2+1):
        if i%j == 0:
            break
        elif i%j != 0 and j == i//2:
            ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
