#https://school.programmers.co.kr/learn/courses/30/lessons/131704
#https://readydeveloperone.blogspot.com/2023/05/131704.html
from collections import deque
def solution(order):
    answer = 0
    truck = []
    sub = []
    main = deque([i for i in range(1, len(order) + 1)])
    for now in order:
        flag = False
        while main:
            le = main.popleft()
            if le > now:
                main.appendleft(le)
                break
            elif le == now:
                truck.append(le)
                flag = True
                break
            elif le < now:
                sub.append(le)
                flag = True
        while sub and not flag:
            ri = sub.pop()
            if ri == now:
                truck.append(ri)
                break
            else:
                answer = len(truck)
                return answer
    answer = len(truck)
    return answer