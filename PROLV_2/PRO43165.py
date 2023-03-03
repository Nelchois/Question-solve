#https://school.programmers.co.kr/learn/courses/30/lessons/43165
op = ['+', '-']
board = []
ans = []
def operation(length):
    if len(board) == length:
        ans.append(''.join(board))
        return 
    for _ in range(len(op)):
        board.append(op[_])
        operation(length)
        board.pop()

def solution(numbers, target):
    answer = 0
    ck_num = 0
    operation(len(numbers))
    for i in range(len(ans)):
        ope = ans[i]
        for j in range(len(ope)):
            if ope[j] == '+':
                ck_num += numbers[j]
            else:
                ck_num -= numbers[j]
        if ck_num == target:
            answer += 1
        ck_num = 0
    return answer