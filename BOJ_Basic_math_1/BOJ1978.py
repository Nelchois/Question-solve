import sys
number = int(sys.stdin.readline().rstrip())
if number != 0:
    num_list = list(set(map(int, sys.stdin.readline().rstrip().split(' '))))
    ck_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    ans = 0
    ans_list = []
    for i in range(len(num_list)):
        ck_num = num_list.pop(0)
        if ck_num in ck_list:
            ans += 1
        elif ck_num == 1:
            continue
        elif ck_num > 31:
            for j in range(10):
                if ck_num%ck_list[j] == 0:
                    break
                elif (ck_num%ck_list[j] != 0) and (j != 9):
                    continue
                elif (ck_num%ck_list[j] != 0) and (j == 9):
                    ans += 1
                    break
    print(ans)
else:
    print(0)