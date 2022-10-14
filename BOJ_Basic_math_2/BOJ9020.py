import sys
case = int(sys.stdin.readline())
num_bol = [True]*10001
for n in range(2, 101):
    if num_bol[n] == True:
        for m in range(n+n, 10001, n):
            num_bol[m] = False
number = [_ for _ in range(2, 10001) if num_bol[_] == True]
for i in range(case):
    ck_num = int(sys.stdin.readline())
    count = 0
    find_list = []
    min_list = []
    ans = []
    while ck_num/2 > number[count]:
        back_num = ck_num - number[count]
        if number[count] <= back_num:
            find_list.append([number[count], back_num])
        if count < len(number):
            count += 1
    for j in range(len(find_list)):
        A, B = find_list[j][0], find_list[j][1]
        if B - A < 0:
            min_list.append(A - B) 
        else:
            min_list.append(B - A)
    idx = min_list.index(min(min_list))
    print(*find_list[idx])
