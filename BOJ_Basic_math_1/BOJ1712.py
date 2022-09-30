import sys
n = 0
A, B, C = map(int, sys.stdin.readline().strip().split(' '))
if B >= C:
    print(-1)
else:
    print(A//(C-B) + 1)
