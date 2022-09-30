import sys
up, down, height = map(int, sys.stdin.readline().rstrip().split())

day = up - down
if (height - up)%day == 0:
    ans = (height - up)//day + 1
else:
    ans = (height - up)//day + 2

print(ans)