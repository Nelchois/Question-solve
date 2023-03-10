#https://school.programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque
st = []
def check(s):
    left = ['[', '{', '(']
    right = [']', '}', ')']
    for i in s:
        if len(st) == 0 and i in right:
            return False
        if i in left:
            st.append(i)
        if i == right[0] and st[-1] == left[0]:
            st.pop()
        elif i == right[1] and st[-1] == left[1]:
            st.pop()
        elif i == right[2] and st[-1] == left[2]:
            st.pop()
    if len(st) == 0:
        return True
    return False
    
def solution(s):
    answer = 0
    s_list = deque(s)
    for i in range(len(s)):
        each = s_list.popleft()
        s_list.append(each)
        if check(s_list) == True:
            answer += 1

    return answer