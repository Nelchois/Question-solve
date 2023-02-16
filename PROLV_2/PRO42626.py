#https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) >= 2:
            min_1 = heapq.heappop(scoville)
            if min_1 >= K:
                break
            min_2 = heapq.heappop(scoville)      
            new_sco = min_1 + 2*min_2
            heapq.heappush(scoville, new_sco)
            answer += 1
            if len(scoville) <= 1:
                if new_sco < K:
                    answer = -1
                break
    return answer