#https://school.programmers.co.kr/learn/courses/30/lessons/12927
from heapq import *
def solution(n, works):
    answer = 0
    q = []
    for num in works:
        heappush(q, [-num, num])
    while n != 0 and q:
        a = heappop(q)
        b = heappop(q)
        dif = a[1] - b[1]
        if dif == 0:
            if n >= 2:
                if a[1] >= 1:
                    a[1] -= 1
                    a[0] += 1
                    b[1] -= 1
                    b[0] += 1
                    n -= 2
            else:
                a[1] -= 1
                a[0] += 1
                n -= 1
        elif dif >= 1:
            if n >= 2:
                if a[1] >= 2:
                    a[1] -= 2
                    a[0] += 2
                    n -= 2
                else:
                    n -= a[1]
                    a[1] = 0
            else:
                if a[1] >= 1:
                    a[1] -= 1
                    a[0] += 1
                    n -= 1
        if a[1] != 0:
            heappush(q, a)
        if b[1] != 0:
            heappush(q, b)
    if len(q) > 0:
        for li in q:
            work = li[1]
            answer += work * work
    return answer