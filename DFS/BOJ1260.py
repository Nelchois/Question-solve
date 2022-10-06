from operator import index
import sys
from collections import deque
num, route, start = map(int, sys.stdin.readline().rstrip().split(' '))
map_dic = dict()
for i in range(route * 2):
    node, way = map(int, sys.stdin.readline().rstrip().split(' '))
    if node in map_dic:
        map_dic[f'{node}'].append(way)
    elif node not in map_dic:
        map_dic[f'{node}'] = [way]
    if way in map_dic:
        map_dic[f'{way}'].append(node)
    elif way not in map_dic:
        map_dic[f'{way}'] = [node]
def DFS(num, map_dic, point):
    ck_point = []
    map_deque = deque()
    while len(ck_point) != num:
        map_deque.append(point)
        now = map_deque.pop()
        if now not in ck_point:
            ck_point.append(now)
        elif now in ck_point:
            now = ck_point[-1]
        ro = map_dic[f'{now}']
        if min(ro) not in ck_point:
            now = min(ro)        
        elif min(ro) in ck_point and max(ro) not in ck_point:
            now = max(ro)
    return ck_point
#a = DFS(num, map_dic, start)
#print(len(a))
print(map_dic)