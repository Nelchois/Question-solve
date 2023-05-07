#https://school.programmers.co.kr/learn/courses/30/lessons/42861#

from collections import deque

def check(connect, n):
    que = deque()
    que.append(connect['0'])
    visit = [False] * n
    visit[0] = True
    while que:
        ma = que.popleft()
        for i in ma:
            key = str(i)
            if visit[i] == False:
                visit[i] = True
                que.append(list(connect[key]))
    return visit

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connect = {f'{i}': set() for i in range(n)}
    costs = deque(costs)
    cost = 0
    for li in costs:
        left, right, c = str(li[0]), str(li[1]), li[2]
        if len(connect[left]) == 0 or len(connect[right]) == 0:
            connect[left].add(int(right))
            connect[right].add(int(left))
            cost += c

    visit = check(connect, n)

    while not all(visit):
        for ma in costs:
            if visit[ma[0]] != visit[ma[1]]:
                cost += ma[2]
                connect[str(ma[0])].add(ma[1])
                connect[str(ma[1])].add(ma[0])
                break
        visit = check(connect, n)

    answer = cost
    return answer