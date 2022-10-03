num_list = list(range(1, 1001))
ck_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ans_list = []
for i in range(len(num_list)):
    num = num_list.pop()
    if num in ck_list:
        ans_list.append(num)
    elif num == 1:
        pass
    else:
        for j in range(len(ck_list)):
            if num%ck_list[j] == 0:
                break
            elif (num%ck_list[j] != 0) and (j != len(ck_list) - 1):
                continue
            else:
                ans_list.append(num)




print(len(ans_list))