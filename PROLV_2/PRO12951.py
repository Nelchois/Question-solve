#https://school.programmers.co.kr/learn/courses/30/lessons/12951
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def solution(s):
    board = []
    answer = []
    word_split = s.split(' ')
    for word in word_split:
        for i in range(len(word)):
            if word[i] in number:
                board.append(word[i])
            elif word[i] in lower:
                if i == 0:
                    board.append(word[i].upper())
                else:
                    board.append(word[i])
            else:
                if i == 0:
                    board.append(word[i])
                else:
                    board.append(word[i].lower())
        if len(board) == len(word):
            answer.append(''.join(board))
            board.clear()
    ans = ' '.join(answer)
    return ans