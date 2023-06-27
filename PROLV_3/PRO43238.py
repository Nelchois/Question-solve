#https://school.programmers.co.kr/learn/courses/30/lessons/43238#
from collections import deque
def solution(n, times):
    times.sort()
    times = deque(times)
    bigt = times.pop()
    if bigt == 1 and len(times) == n - 1:
        return 1
    times.append(bigt)
    t = times.popleft()
    mint, maxt = t*1, t*n
    times.appendleft(t)
    while True:
        done = 0
        midt = (mint + maxt) // 2 
        for i in times:
            done += midt//i
        if done >= n:
            maxt = midt
        elif done < n:
            mint = midt
        if mint == maxt - 1:
            break
    return maxt