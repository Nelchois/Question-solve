#https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    answer = []
    if s == 1:
        if n == 1:
            return [1]
        else:
            return [-1]
    if n > s:
        return [-1]
    share, left = divmod(s, n)
    for i in range(n):
        answer.append(share)
    idx = -1
    while left != 0:
        answer[idx] += 1
        left -= 1
        idx -= 1
    return answer
