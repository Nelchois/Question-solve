#https://school.programmers.co.kr/learn/courses/30/lessons/84512
board = []
words = []
alpha = ['A', 'E', 'I', 'O', 'U']
def make(word, alpha, n):
    if len(board) == n:
        words.append(''.join(board))
        return
    for i in range(len(alpha)):
        board.append(alpha[i])
        make(word, alpha, n)
        board.pop()


def solution(word):
    answer = 0
    for num in range(1, 6):
        make(word, alpha, num)
    words.sort(key = lambda x:x)
    for idx in range(len(words)):
        if words[idx] == word:
            answer += idx + 1
            break
    return answer