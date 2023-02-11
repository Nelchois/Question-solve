#https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(list(enumerate(priorities)))
    while True:
        doc = priorities.popleft()
        if len(priorities) == 0:
            answer += 1
            break
        le_max = max(priorities, key = lambda x:x[1])
        if doc[1] >= le_max[1]:
            answer += 1
            if location == doc[0]:
                break
        else:
            priorities.append(doc)        
    return answer