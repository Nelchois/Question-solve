#https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = ''
    board = []
    for num in number:
        while len(board) != 0 and board[-1] < num and k > 0:
            k -= 1
            board.pop()
        board.append(num)
    if k != 0:
        board = board[: -k]
    answer = answer.join(board)
    return answer