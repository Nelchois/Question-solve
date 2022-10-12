import sys
N = int(sys.stdin.readline())
num = []
if N != 1:
    ck_num = N
    for i in range(2, N+1):
        while ck_num%i == 0:
            ck_num = ck_num/i
            num.append(i)
sorted(num)
print(*num, sep='\n')
