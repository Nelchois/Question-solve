#https://school.programmers.co.kr/learn/courses/30/lessons/42628
from heapq import *
def solution(operations):
    answer = []
    q = []
    for command in operations:
        if command[0] == 'I':
            num = command[1:]
            if num[0] == '-':
                num = -int(num[1:])
            else:
                num = int(num)
            heappush(q, num)
        if command[0] == 'D':
            if len(q) == 0:
                continue
            if '-' in command:
                heappop(q)
            else:
                left = []
                for _ in range(len(q)):
                    a = heappop(q)
                    if len(q) > 0:
                        heappush(left, a)
                q = left
    if len(q) == 0:
        answer.append(0)
        answer.append(0)
    else:
        a = heappop(q)
        for _ in range(len(q)):
            b = heappop(q)
            if len(q) == 0:
                answer.append(b)
        answer.append(a)
    return answer