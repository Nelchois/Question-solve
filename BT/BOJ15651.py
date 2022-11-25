import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
ans = []
def number():
    if len(ans) == m:
        print(*ans)
    else:
        for num in range(1, n + 1):
            ans.append(num)
            number()
            ans.pop()
number()