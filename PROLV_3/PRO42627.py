#https://school.programmers.co.kr/learn/courses/30/lessons/42627#
from heapq import *
from collections import deque
def solution(jobs):
    answer = 0
    jobs.sort()
    time, heap = 0, []
    for start, delay in jobs:
        while start >= time and len(heap) > 0:
            d, s = heappop(heap)
            if time < s:
                time = s + d
                answer += d
            else:
                time = time + d
                answer += time - s
        else:
            heappush(heap, [delay, start])

    while heap:
        delay, start = heappop(heap)
        time = time + delay
        answer += time - start
    return answer//len(jobs)