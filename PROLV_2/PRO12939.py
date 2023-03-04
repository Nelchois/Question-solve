#https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    number = s.split(' ')
    answer_list = []
    for num in number:
        if '-' in num:
            answer_list.append(0-int(num[1:]))
        else:
            answer_list.append(int(num))
            
    answer = f'{min(answer_list)} {max(answer_list)}'
    return answer