import sys
num = int(sys.stdin.readline().rstrip())
count = 0
for i in range(num):
    case_word = list(sys.stdin.readline().rstrip()) 
    repeat_num = len(case_word)   
    Q = []
    for _ in range(repeat_num):
        check_str = case_word.pop(0)
        Q.append(check_str)
        if len(case_word) != 0:
            if check_str == case_word[0]:
                pass
            elif check_str != case_word[0]:
                if case_word[0] not in Q:
                    pass
                elif case_word[0] in Q:
                    break

        elif (len(case_word) == 0) and (len(Q) >= 1):
            count += 1
        
print(count)