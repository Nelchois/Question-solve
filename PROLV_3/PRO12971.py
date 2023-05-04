#https://school.programmers.co.kr/learn/courses/30/lessons/12971
from collections import deque
def dp(sticker):
    if len(sticker) > 2:
        ans = [0, 0]
        for num in sticker:
            ans = [max(ans), ans[0] + num]
        max_num = max(ans)
    else:
        max_num = max(sticker)

    return max_num

def solution(sticker):
    answer = 0
    if len(sticker) <= 2:
        return max(sticker)
    sticker = deque(sticker)
    second = []
    for n in sticker:
        second.append(n)
    second.pop()
    sticker.popleft()
    a = dp(sticker)
    b = dp(second)
    if a > b:
        answer = a
    else:
        answer = b 

    return answer
