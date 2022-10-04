import sys

count = int(sys.stdin.readline().rstrip())
ck_array = []
for i in range(count):
    ck_array.append(int(sys.stdin.readline().rstrip()))
a = sorted(ck_array)
for _ in range(count):
    print(a[_])