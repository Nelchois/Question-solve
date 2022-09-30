import sys
ck_num = int(sys.stdin.readline())
i = 0
while True:
    if ck_num == 1:
        print(1)
        break
    elif (3*i*(i-1)+2 <=ck_num <= 3*i*(i+1)+1) and (ck_num != 1):
        print(i+1)
        break
    else:
        i += 1
