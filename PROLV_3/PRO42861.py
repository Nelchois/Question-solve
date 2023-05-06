from collections import deque

def check(visit, connect, n, que):
    while que:
        ma = que.popleft()
        for i in ma:
            ck = str(i)
            if ck not in visit:
                visit[ck] = True
                que.append(connect[ck])
    if len(visit) == n:
        return True
    return False

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connect = {f'{i}': set() for i in range(n)}
    costs = deque(costs)
    cost = 0
    start_point = 0
    for li in costs:
        key = str(li[0])
        son = str(li[1])
        que = deque()
        if start_point == 0:
            connect[key].add(int(son))
            que.append(connect[key])
            start_point = key
            
        visit = dict()
        while que:
            ma = que.popleft()
            for i in ma:
                ck = str(i)
                if ck not in visit:
                    visit[ck] = True
                    if len(connect[ck]) > 0:
                        que.append(connect[ck])
        
        if len(visit) == n:
            cost += li[2]
            break
        
        if son not in visit:
            connect[key].add(int(son))
            cost += li[2]
        
            
    print(costs)
    print(cost)
    return answer