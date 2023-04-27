#https://school.programmers.co.kr/learn/courses/30/lessons/12987
from heapq import *
def solution(A, B):
    answer = 0
    heapify(A)
    heapify(B)
    while True:
        if len(A) == 0 or len(B) == 0:
            break
        a, b = heappop(A), heappop(B)
        if a >= b:
            for i in range(len(B)):
                ck = heappop(B)
                if a < ck:
                    answer += 1
                    break
        else:
            answer += 1
    return answer