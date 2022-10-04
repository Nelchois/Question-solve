import sys
count = int(sys.stdin.readline().rstrip())
num_list = [0]*10000
for i in range(count):
    ele = int(sys.stdin.readline())
    num_list[ele-1] += 1
for i in range(10000):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i+1)