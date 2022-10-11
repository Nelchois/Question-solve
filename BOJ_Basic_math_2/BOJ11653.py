import sys
N = int(sys.stdin.readline())
num = []
if N != 1:
    for i in range(N):
        if i != 0 and i != 1:
            if N%i == 0:
                num.append(i)
sorted(num)
print(*num, sep='\n')
