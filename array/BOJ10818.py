import sys
A = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(' ')))
print(f'{min(B)} {max(B)}')

