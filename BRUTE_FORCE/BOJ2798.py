import sys
from itertools import combinations
card, m = map(int, sys.stdin.readline().rstrip().split(' '))
num = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ans = []
result = list(combinations(num, 3))
for i in range(len(result)):
    s = sum(result[i])
    if s <= m:
        ans.append(s)
print(max(ans))