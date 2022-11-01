import sys
str_num = sys.stdin.readline().rstrip()
int_num = int(str_num)
length = len(str_num)
ans = []
def ck_number(num):
    if num <= 0 or num < int_num - length*9:
        return num
    else:
        ck_str = str(num)
        num_list = []
        for i in range(len(ck_str)):
            num_list.append(int(ck_str[i]))
        if num + sum(num_list) == int_num:
            ans.append(num)
        return ck_number(num - 1)
a = ck_number(int_num)
if len(ans) > 0:
    print(min(ans))
elif len(ans) == 0:
    print(0)