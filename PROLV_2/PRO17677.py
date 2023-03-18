#https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    str_dict = dict()
    str_list = []
    for i in range(len(str1) - 1):
        case = str1[i: i + 2]
        upcase = case.upper()
        if upcase.isalpha() == True:
            str_list.append(upcase)
            if upcase not in str_dict:
                str_dict[upcase] = [1, 0]
            else:
                str_dict[upcase][0] += 1
    for i in range(len(str2) - 1):
        case2 = str2[i: i + 2]
        upcase2 = case2.upper()
        if upcase2.isalpha() == True:
            str_list.append(upcase2)
            if upcase2 in str_dict:
                str_dict[upcase2][1] += 1
            else:
                str_dict[upcase2] = [0, 1]
    min_num = []
    max_num = []
    for j in str_dict:
        case_j = str_dict[j]
        min_num.append(min(case_j))
        max_num.append(max(case_j))
    a = sum(min_num)
    b = sum(max_num)
    if b == 0:
        sim = 1
    else:
        sim = a / b
    answer = sim * 65536
    return int(answer)
