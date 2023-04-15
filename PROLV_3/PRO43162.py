#https://school.programmers.co.kr/learn/courses/30/lessons/43162
board = []
net = set()
def dfs(n, num, computers):
    for i in range(n):
        if computers[num][i] == 1 and i not in board:
            board.append(i)
            dfs(n, i, computers)
        
def solution(n, computers):
    for j in range(n):
        if j not in board:
            board.append(j)
            dfs(n, board[-1], computers)
        net.add(tuple(board))
    answer = len(net)
    return answer
