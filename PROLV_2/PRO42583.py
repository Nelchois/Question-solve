#https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque
def add(n):
    return n + 1
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque()
    time = 0
    now = weight
    t_list = deque()
    while True:
        if len(bridge) == 0 and len(truck_weights) == 0:
            break
            
        if len(bridge) > 0 and bridge[0] == bridge_length:
            bridge.popleft()
            now += t_list.popleft() 
                
        if len(truck_weights) > 0 and now >= truck_weights[0]:
            truck = truck_weights.popleft()
            bridge.append(0)
            t_list.append(truck)
            now -= truck 
            
        bridge = deque(map(add, bridge))
        time += 1
        
    answer = time
    return answer