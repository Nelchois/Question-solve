import sys
def check():
    n = int(sys.stdin.readline())
    count = 0
    if n < 10:
        count += n
    elif 10 <= n <100:
        count += n
    elif 100 <= n < 1000:
        count += n_1000(n)

    return print(count)

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
        elif ((i%100) > 10) and (i >= 100):
            A = (i//100)
            B = (i%100)//10
            C = (i%10)
            if (A-B) == (B-C):
                count += 1
            else:
                continue
    return print(count)

n_1000()