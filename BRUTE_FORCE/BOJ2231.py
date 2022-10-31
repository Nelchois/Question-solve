import sys
str_num = sys.stdin.readline().rstrip()
int_num = int(str_num)
length = len(str_num)
ans = []
def ck_number(num):
    if num == int_num - length*9:
        return num
    else:
        num
        return ck_number(num - 1)

