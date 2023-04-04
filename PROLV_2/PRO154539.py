#https://school.programmers.co.kr/learn/courses/30/lessons/154539
from heapq import *
def solution(numbers):
    heap = []
    answer = [-1 for i in range(len(numbers))]
    for idx, num in enumerate(numbers):
        while heap and heap[0][0] < num:
            val, i = heappop(heap)
            answer[i] = num
        heappush(heap, [num, idx])
    return answer