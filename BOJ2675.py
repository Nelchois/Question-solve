import sys
case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    case_list = list(sys.stdin.readline().rstrip().split(' '))
    repeat_num = int(case_list.pop(0))
    repeat_str = case_list.pop(0)
    ans = ''
    for i in range(len(repeat_str)):
        ans += repeat_num*repeat_str[i]
    print(ans)