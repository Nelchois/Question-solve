#https://school.programmers.co.kr/learn/courses/30/lessons/72413
from heapq import *
def Dij(start, route, n):
    distance = {str(i) : -1 for i in range(1, n + 1)}
    distance[str(start)] = 0
    heap = []
    heappush(heap, [distance[str(start)], start])
    while heap:
        now_dis, now_node = heappop(heap)
        if distance[str(now_node)] < now_dis:
            continue
        ck_route = route[str(now_node)]
        for rou in ck_route:
            key = str(rou)
            new_dis = now_dis + ck_route[key]
            if distance[key] == -1:
                distance[key] = new_dis
                heappush(heap, [distance[str(key)], rou])
            elif distance[key] > new_dis:
                distance[key] = new_dis
                heappush(heap, [distance[str(key)], rou])

    return distance
def solution(n, s, a, b, fares):
    answer = 0
    route = {str(i): {} for i in range(1, n + 1)}
    for f in fares:
        x, y, z = f
        route[str(x)][str(y)] = z
        route[str(y)][str(x)] = z
    
    base = Dij(s, route, n)
    if base[str(b)] != -1 and base[str(a)] != -1:
        fee = base[str(a)] + base[str(b)]
    else:
        fee = -1
    for num in range(1, n + 1):
        if num != s:
            ck_di = Dij(num, route, n)
            a_f, a_b = ck_di[str(a)], ck_di[str(b)]
            if base[str(num)] == -1:
                continue
            if a_f != -1 and a_b != -1:
                new_fee = a_f + a_b + base[str(num)]
                if fee > new_fee:
                    fee = new_fee
    
    answer = fee
    return answer