import sys
from collections import deque
''' prototype
num, route, point = map(int, sys.stdin.readline().rstrip().split(' '))
map_list = []
for i in range(route):
    node, way = map(int, sys.stdin.readline().rstrip().split(' '))
    map_list.append((node, way))
    map_list.append((way, node))
map_dict = defaultdict(list)
for k, v in map_list:
    map_dict[k].append(v)

def DFS(num, map_dict, point):
    ck_point = []
    map_deque = deque()
    while True:
        if len(ck_point) == len(map_dict):
            break
        if len(map_deque) == 0:
            map_deque.append(point)
            now = map_deque.pop()
            if now not in ck_point:
                ck_point.append(now)
            map_deque.append(max(map_dict[now]))
            map_deque.append(min(map_dict[now]))
        elif len(map_deque) != 0:
            now = map_deque.pop()
            if now not in ck_point:
                ck_point.append(now)
            way1 = max(map_dict[now])
            way2 = min(map_dict[now])
            if way1 in ck_point and way2 in ck_point:
                continue
            elif way1 in ck_point and way2 not in ck_point:
                map_deque.append(way2)
            elif way1 not in ck_point and way2 in ck_point:
                map_deque.append(way1)
    return ck_point
def BFS(num, map_list, point):
    ck_point2 = []
    map_deque = deque()
    while True:
        if len(ck_point2) == len(map_list):
            break
        if len(map_deque) == 0:
            map_deque.append(point)
            now = map_deque.popleft()
            map_deque.append(min(map_list[now]))
            map_deque.append(max(map_list[now]))
            ck_point2.append(now)
        elif len(map_deque) != 0:
            now = map_deque.popleft()
            if now not in ck_point2:
                ck_point2.append(now)
            elif now in ck_point2: 
                continue   
            if len(map_list[now]) > 1:
                way1 = max(map_list[now])
                way2 = min(map_list[now])
                if way1 in ck_point2 and way2 not in ck_point2:
                    map_deque.append(way2)
                elif way2 in ck_point2 and way1 not in ck_point2:
                    map_deque.append(way1)
            elif len(map_list[now]) == 1:
                way = map_list[now]
                if way not in ck_point2:
                    map_deque.append(way)
    return ck_point2
print(*DFS(num, map_dict, point))
print(*BFS(num, map_dict, point))
'''
n, m, v = map(int, sys.stdin.readline().rstrip().split())

adj = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(v, hist, adj):
    hist.append(v)
    for i in range(1, n + 1):
        if adj[v][i] and i not in hist:
            hist = dfs(i, hist, adj)
    return hist

def bfs(v, adj):
    q = [v]
    hist = [v]
    while q:
        now = q.pop(0)
        for i in range(1, n + 1):
            if adj[now][i] and i not in hist:
                q.append(i)
                hist.append(i)
    return hist

print(*dfs(v, [], adj))
print(*bfs(v, adj))