#https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    n = len(citations)
    for idx, h in enumerate(citations):
        idx += 1
        if idx == h:
            return idx
        elif idx > h:
            return idx -1
    return n

