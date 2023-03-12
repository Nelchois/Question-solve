#https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []
    col = len(arr1[0])
    for arr in arr1:
        board = []
        for row in range(len(arr2[0])):
            ele = 0
            for i in range(col):
                ele += arr[i] * arr2[i][row]
            board.append(ele)
        answer.append(board)

    return answer

