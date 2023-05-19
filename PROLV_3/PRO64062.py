#https://school.programmers.co.kr/learn/courses/30/lessons/64062#
#https://readydeveloperone.blogspot.com/2023/05/64062.html (Korean explain of how to solve)
from collections import deque
def solution(stones, k):
    answer = 200000001
    que = deque()
    if len(stones) <= 1:
        if len(stones) == 1:
            answer = stones.pop()
        return answer
    for i, stone in enumerate(stones):
        if len(que) == 0:
            que.append([stone, i])
            continue
        while que:
            right = que.pop()
            if stone < right[0]:
                que.append(right)
                break
        que.append([stone, i])
        while que:
            left = que.popleft()
            if i + 1 - k <= left[1] <= i + k:
                que.appendleft(left)
                break
        if i + 1 >= k:
            m = que.popleft()
            answer = min(answer, m[0])
            que.appendleft(m)
    return answer