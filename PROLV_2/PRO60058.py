#https://school.programmers.co.kr/learn/courses/30/lessons/60058
from collections import deque
def complete(l):
    que = deque()
    for i in l:
        if i == '(':
            que.append(i)
        else:
            if len(que) > 0:
                que.pop()
            else:
                return False
    return True
def change(o):
    if len(o) == 0:
        return ''
    u = ""
    left, right = deque(), deque()
    que = deque()
    flag = True
    if complete(o):
        return o
    for i in o:
        u += i
        if i == '(':
            left.append(i)
        else:
            right.append(i)
        if len(left) == len(right):
            break
    v = o[len(u): ]
    if complete(u) == True:
        return u + change(v)
    else:
        new = ""
        for i in u[1: len(u) - 1]:
            if i == '(':
                new += ')'
            elif i == ')':
                new += '('
        return '(' + change(v) + ')' + new
    
def solution(p):
    answer = ''
    o = "".join(p)
    que = deque()
    answer = change(o)
    return answer