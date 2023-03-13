#https://school.programmers.co.kr/learn/courses/30/lessons/42578



def solution(clothes):
    clo = dict()
    for part in clothes:
        category = part[1]
        if category in clo:
            clo[f'{category}'] += 1
        else:
            clo[f'{category}'] = 1
    num = list(clo.values())
    answer = 1
    for i in num:
        answer *= (i+1)
    
    
    return answer - 1