#https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    board = []
    match = 0
    while True:
        if len(answer) != 0:
            break
        for player in range(n):
            idx = player + (match * n)
            if idx >= len(words):
                answer.append(0)
                answer.append(0)
                break
            word = words[idx]
            if len(board) == 0:
                board.append(word)
            elif len(board) != 0:
                if word in board:
                    answer.append(player + 1)
                    answer.append(match + 1)
                    break
                elif board[-1][-1] != word[0]:
                    answer.append(player + 1)
                    answer.append(match + 1)
                    break
                else:
                    board.append(word)
        match += 1
    return answer