#https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque
def solution(n, edge):
    answer = 0
    map_dict = dict()
    edge.sort(key = lambda x:x[0])
    length = dict()
    length[str(1)] = 0
    edge = deque(edge)
    while edge:
        ma = edge.popleft()
        mother = str(ma[0])
        son = str(ma[1])
        if mother in length and son not in length:
            length[son] = length[mother] + 1
        elif mother not in length:
            length[mother] = length[son] + 1
            
    """for i in range(1, len(map_dict)+1):
        ma = map_que.popleft()
        mother = str(i)
    """    
    print(length)
    ans = list(length.values())
    answer = ans.count(max(ans))
    return answer