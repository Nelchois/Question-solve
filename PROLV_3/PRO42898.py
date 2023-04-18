#https://school.programmers.co.kr/learn/courses/30/lessons/42898#
def solution(m, n, puddles):
    board = [[0 for i in range(m)] for i in range(n)]
    board[0][0] = 1
    for y, x in puddles:
        board[x-1][y-1] = 1
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0):
                continue
            if board[i][j] > 0:
                board[i][j] = 0
            else:
                a = i - 1
                b = j - 1
                if a < 0:
                    a = 0
                if b < 0:
                    b = 0
                board[i][j] = (board[a][j] + board[i][b]) 

    answer = board[-1][-1] % 1000000007
    return answer
