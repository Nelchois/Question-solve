import sys
ck_num = int(sys.stdin.readline())

line = 0

while ck_num > line:
    ck_num -= line
    line += 1
if line%2 == 0:
    print(ck_num, '/', line-ck_num+1, sep='')
else:
    print(line-ck_num+1, '/', ck_num, sep='')