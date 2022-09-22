import sys
A = []
B = []
for _ in range(10):
    A.append(int(sys.stdin.readline().rstrip()))
for _ in range(10):
    left = A[_] % 42
    B.append(left)
print(len(set(B)))