#https://school.programmers.co.kr/learn/courses/30/lessons/43164
board = ["ICN"]
def dfs(airport, route, air, ans_list):
    now = list(airport[air])
    for i in now:
        r = air + i
        if route[r] != 0:
            route[r] -= 1
            board.append(i)
            if sum(list(route.values())) == 0:
                ans_list.append(tuple(board))
            if i in airport:
                dfs(airport, route, i, ans_list)
            board.pop()
            route[r] += 1
def solution(tickets):
    answer = []
    airport = dict()
    route = dict()
    for ro in tickets:
        air1, air2 = ro[0], ro[1]
        air = air1 + air2
        if air not in route:
            route[air] = 1
        else:
            route[air] += 1
        if air1 not in airport:
            airport[air1] = {air2}
        else:
            airport[air1].add(air2)
    ans_list = []
    dfs(airport, route, "ICN", ans_list)
    ans_list.sort(reverse = True)
    answer = list(ans_list.pop())
    return answer