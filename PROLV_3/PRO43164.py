#https://school.programmers.co.kr/learn/courses/30/lessons/43164
board = ["ICN"]

def dfs(airport, route, air, ans_list):
    if len(board) == len(airport):
        print(board)
        #ans_list.append(tuple(board))
        return
    now = list(route[air])
    for i in now:
        if airport[i] == False:
            airport[i] = True
            board.append(i)
            dfs(airport, route, i, ans_list)
            board.pop()
            airport[i] = False

def solution(tickets):
    answer = []
    airport = dict()
    route = dict()
    for ro in tickets:
        air1 = ro[0]
        air2 = ro[1]
        if air1 not in airport:
            airport[air1] = False
        if air2 not in airport:
            airport[air2] = False
        if air1 not in route:
            route[air1] = {air2}
        else:
            route[air1].add(air2)
        if air2 not in route:
            route[air2] = {air1}
        else:
            route[air2].add(air1)
    ans_list = []
    airport["ICN"] = True
    dfs(airport, route, "ICN", ans_list)
    #print(ans_list)
    return answer