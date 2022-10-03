import sys
test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    floor = list(range(1, 15))
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    for i in range(k):
        ck_floor = []
        for j in range(n):
            if j > 0:
                ck_floor.append(sum(floor[:j+1]))
            elif j == 0 :
                ck_floor.append(1)
        floor = ck_floor
    print(floor[n-1])




