#https://school.programmers.co.kr/learn/courses/30/lessons/17687
import string
from collections import deque
def convert(number, b):
    st = string.digits+string.ascii_uppercase
    number, share = divmod(number, b)
    if number == 0 :
        return st[share] 
    else :
        return convert(number, b) + st[share]
    
def solution(n, t, m, p):
    answer = ''
    totalList = deque()
    now_num = 0
    limit = t * m + 1
    while len(totalList) < limit:
        if now_num < n:
            totalList.append(str(now_num))
            now_num += 1
        else:
            based_num = convert(now_num, n)
            for i in based_num:
                totalList.append(i)
            now_num += 1
    for i in range(1, limit):
        now_turn = totalList.popleft()
        if i == p:
            if now_turn == "10":
                answer += 'A'
            elif now_turn == "11":
                answer += 'B'
            elif now_turn == "12":
                answer += 'C'
            elif now_turn == "13":
                answer += 'D'
            elif now_turn == "14":
                answer += 'E'
            elif now_turn == "15":
                answer += 'F'
            else:
                answer += now_turn
            p += m
        
    return answer
