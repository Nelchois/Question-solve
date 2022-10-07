import sys
num, route, point = map(int, sys.stdin.readline().rstrip().split(' '))
map_list = dict()
for i in range(route):
    node, way = map(int, sys.stdin.readline().rstrip().split(' '))
    map_list[list[node][0]] += [list[way][0]]
print(map_list)