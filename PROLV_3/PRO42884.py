#https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    cam = []
    routes.sort(key = lambda x: x[1])
    for i in range(len(routes)):
        road = routes[i]
        if len(cam) == 0:
            cam.append(road[1])
        else:
            ck = False
            for c in cam:
                if road[0] <= c <= road[1]:
                    ck = True
                    break
            if ck == False:
                cam.append(road[1])
    answer = len(cam)
    return answer