#https://school.programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    board = land
    for i in range(1, len(land)):
        for j in range(4):
            board[i][j] += max(board[i-1][:j] + board[i-1][j+1:])
    answer = max(board.pop())
    return answer