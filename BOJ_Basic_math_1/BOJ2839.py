import sys
sugar = int(sys.stdin.readline().rstrip())
ck_num = 1
counter = 0
if sugar % 5 == 0: 
    print(sugar // 5)
else:
    while sugar > 0:
        sugar -= 3
        counter += 1
        if sugar % 5 == 0: 
            counter += sugar // 5
            print(counter)
            break
        elif sugar <= 2:
            print(-1)
            break
        elif sugar == 0:  
            print(counter)
            break


