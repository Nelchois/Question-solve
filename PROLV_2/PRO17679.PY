#https://school.programmers.co.kr/learn/courses/30/lessons/17679
from collections import deque
from string import ascii_uppercase
def solution(m, n, board):
    answer = 0
    a = list(ascii_uppercase)
    alpha = dict()
    for alp in a:
        alpha[alp] = 0
    new_board = list(map(list, zip(*board)))[::-1]
    new_board = deque(new_board)
    x, y = len(new_board), len(new_board[0])
    for _ in range(m+n):
        idx_list = []
        for i in range(x-1):
            for j in range(y-1):
                ch = new_board[i][j]
                if ch not in alpha:
                    continue
                ch_1 = new_board[i+1][j]
                ch_2 = new_board[i][j+1]
                ch_3 = new_board[i+1][j+1]
                if ch == ch_1 and ch == ch_2 and ch == ch_3:
                    idx_list.append((i, j))
                    idx_list.append((i+1, j))
                    idx_list.append((i, j+1))
                    idx_list.append((i+1, j+1))
        for tu in idx_list:
            t1, t2 = tu[0], tu[1]
            new_board[t1][t2] = 0
        for _ in range(x):
            li = deque(new_board.popleft())
            while 0 in li:
                li.remove(0)
            for q in range(y - len(li)):
                li.appendleft(0)
            new_board.append(li)
    for line in new_board:
        answer += line.count(0)
    return answer