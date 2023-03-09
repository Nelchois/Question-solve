#https://school.programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    s1 = 1
    s2 = 2
    for i in range(n-2):
        s1, s2 = s2, s1 + s2
    answer = s2 % 1234567
    return answer
