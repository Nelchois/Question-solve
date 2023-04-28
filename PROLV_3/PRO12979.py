#https://school.programmers.co.kr/learn/courses/30/lessons/12979
from collections import deque
def solution(n, stations, w):
    answer = 0
    stations = deque(stations)
    length = 2*w + 1
    now = 1
    while stations:
        g = stations.popleft()
        left, right = g - w, g + w
        if left > now:
            need = left - now
            if need > length:
                a, b = divmod(need, length)
                if b > 0:
                    answer += a + 1
                else:
                    answer += a
            else:
                answer += 1
        now = right + 1
        if len(stations) == 0:
            fin = n - now + 1
            if fin > 0:
                c, d = divmod(fin, length)
                if d > 0:
                    answer += c + 1
                else:
                    answer += c
    return answer