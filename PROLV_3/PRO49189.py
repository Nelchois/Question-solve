#https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def solution(n, edge):
    answer = 0
    map_dict = {f'{i}' : [] for i in range(1, n + 1)}
    edge.sort(key = lambda x:x[0])
    for m in edge:
        top, bot = m[0], m[1]
        map_dict[str(top)].append(bot)
        map_dict[str(bot)].append(top)
    visit = dict()
    length = dict()
    length['1'] = 0
    visit['1'] = True
    mapq = deque()
    mapq.append(map_dict['1'])
    mapq[0].append(1)

    while mapq:
        ma = mapq.popleft()
        now = str(ma.pop())
        for i in ma:
            node = str(i)
            if node not in visit:
                visit[node] = True
                next_ma = map_dict[node]
                next_ma.append(i)
                mapq.append(next_ma)
                length[node] = length[now] + 1
            else:
                if length[now] + 1 < length[node]:
                    length[node] = length[now] + 1

    if len(visit) < n-1:
        answer = n - len(visit)
    else:
        ans = list(length.values())
        answer = ans.count(max(ans))
    return answer