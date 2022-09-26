import sys
check = sys.stdin.readline().rstrip()
if '0' <= check <= '9':
    check == int(check)
print(ord(check))