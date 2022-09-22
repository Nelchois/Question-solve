import sys
case_num = int(sys.stdin.readline().rstrip())
case_list = []
for _ in range(case_num):
    case_list.append(sys.stdin.readline().rstrip())
for i in case_list:
    counter = 0
    score = 0
    for j in range(len((i))):
        check_str = i[j]
        if check_str == 'O':
            counter += 1
            score += counter 
        elif check_str == 'X':
            counter = 0
    print(score)




