import sys
number = list(map(int, sys.stdin.readline().rstrip()))
ans = sorted(number, reverse=True)
print(*ans, sep='')