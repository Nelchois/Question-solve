import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
number_list = [i for i in range(1, n + 1)]
ans = []
def number():
    if len(ans) == m:
        print(ans)
        return
    for num in number_list:
        if num not in ans:
            ans.append(num)
            number()
            ans.pop()
number()