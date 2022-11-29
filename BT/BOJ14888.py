import sys
import math
size = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().rstrip().split(' ')))
operations = list(map(int, sys.stdin.readline().rstrip().split(' ')))
cal_case = []
ans = []
board = []
def cal():
    if len(cal_case) == size - 1:
        for i in range(len(cal_case)):
            if cal_case[i] == '+':
                if i == 0:
                    board.append(number[0] + number[1])
                else:
                    board[0] += number[i + 1]
            elif cal_case[i] == '-':
                if i == 0:
                    board.append(number[0] - number[1])
                else:
                    board[0] -= number[i + 1]
            elif cal_case[i] == '*':
                if i == 0:
                    board.append(number[0] * number[1])
                else:
                    board[0] *= number[i + 1]
            elif cal_case[i] == '/':
                if i == 0:
                    board.append(math.trunc(number[0] / number[1]))
                else:
                    board[0] = math.trunc(board[0] / number[i + 1])
        ans.append(board[0])
        board.pop()
        return
    for idx in range(4):
        if operations[idx] >= 1:
            if idx == 0 and cal_case.count('+') < operations[0]:
                cal_case.append('+')
                cal()
                cal_case.pop()
            elif idx == 1 and cal_case.count('-') < operations[1]:
                cal_case.append('-')
                cal()
                cal_case.pop()
            elif idx == 2 and cal_case.count('*') < operations[2]:
                cal_case.append('*')
                cal()
                cal_case.pop()
            elif idx == 3 and cal_case.count('/') < operations[3]:
                cal_case.append('/')
                cal()
                cal_case.pop()
cal()
print(max(ans), min(ans), sep= '\n')
