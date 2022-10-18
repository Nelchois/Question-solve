import sys
case = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().rstrip().split(' ')))
set_num = sorted(number)
num_dict = dict()
for i in range(len(set_num)):
    ck = set_num[i]
    if f'{ck}' in num_dict:
        continue
    else:
        num_dict[f'{ck}'] = len(num_dict)
ans = [num_dict[f'{i}'] for i in number]
print(*ans)
