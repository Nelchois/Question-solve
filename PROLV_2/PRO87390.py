#https://school.programmers.co.kr/learn/courses/30/lessons/87390
def solution(n, left, right):
    idx = 0
    answer = []
    for i in range(left, right + 1):
        sh = i // n
        le = i % n
        answer.append(max(sh, le) + 1)
    return answer