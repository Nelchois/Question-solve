import sys
def n_1000():
    n = int(sys.stdin.readline())
    count = 0
    for i in range(1, n+1):
        if (i < 10):
            count += 1
        elif (10 <= i < 100):
            count += 1
        elif ((i%100) < 10) and (i >= 100):
            continue
        elif ((i%100) >= 10) and (i >= 100):
            A = (i//100)
            B = (i%100)//10
            C = (i%10)
            if (A-B) == (B-C):
                count += 1
            else:
                continue
    return print(count)

n_1000()