#https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
def search(route, n):
    deque = []
    dx, dy, dm = [-1, 0, 1, 0], [0, -1, 0, 1], ['U', 'L', 'D', 'R']
    deque.append([0, 0, 0, 0])

    history = {f'{k}': {} for k in range(n)}
    
    while deque:
        price, x, y, move = deque.pop()
        for i in range(4):
            nx, ny, nm = x + dx[i], y + dy[i], dm[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
                if route[nx][ny] != 1:
                    c = 100
                    if move != nm:
                        c += 500
                    np = price + c
                    if str(ny) not in history[str(nx)] or history[str(nx)][str(ny)] >= np:
                        history[str(nx)][str(ny)] = np
                    else:
                        continue
                    deque.append([np, nx, ny, nm])
    return history[str(n - 1)][str(n - 1)]
def solution(board):
    
    n = len(board)
    a = search(board, n)
    answer = a - 500
    return answer
