import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
number_list = [i for i in range(1, n + 1)]
ans = []
sort_ck = []
def number():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for num in range(1, n + 1):
        if len(ans) == 0:
            if num not in ans:
                ans.append(num)
                number()
                ans.pop()
        else:
            if num not in ans and num > ans[-1]:
                ans.append(num)
                number()
                ans.pop()
number()

