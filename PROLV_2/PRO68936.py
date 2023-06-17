from collections import deque
def count(arr, n, answer, changer):
    checker = {'0': [1, 0], '1': [3, 1], '2': [2, 2], '3': [1, 3], '4': [0, 1]}
    board = deque()
    for x in range(n):
        for y in range(n):
            alpha = arr[x][y]
            k = str(alpha)
            if alpha != 'X':
                if x % 2 == 0:
                    if y % 2 == 0:
                        if arr[x + 1][y + 1] != 'X':
                            arr[x + 1][y + 1] += alpha
                    else:
                        if arr[x + 1][y] != 'X':
                            arr[x + 1][y] += alpha
                else:
                    if y % 2 == 0:
                        if arr[x][y + 1] != 'X':
                            arr[x][y + 1] += alpha
                    else:
                        if k == '0':
                            board.append(0)
                            if changer == False:
                                answer[0] -= 3
                        elif k == '4':
                            board.append(1)
                            if changer == False:
                                answer[1] -= 3
                        else:
                            board.append('X')
                        if changer == True:
                            answer[0] += checker[k][0]
                            answer[1] += checker[k][1]  
            elif alpha == 'X':
                if x % 2 == 0:
                    if y % 2 == 0:
                        arr[x + 1][y + 1] = 'X'
                    else:
                        arr[x + 1][y] = 'X'
                else:
                    if y % 2 == 0:
                        arr[x][y + 1] = 'X'
                    else:
                        board.append('X')
    return board, n//2

def reshape(arr, n):
    b = [[] for _ in range(n)]
    cnt = 0
    idx = 0
    while arr:
        ele = arr.popleft() 
        b[idx].append(ele)
        cnt += 1
        if cnt == n:
            idx += 1
            cnt = 0
    return b
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    changer = True
    b, n = count(arr, n, answer, changer)
    while n != 2:
        changer = False
        b = reshape(b, n)
        b, n = count(b, n, answer, changer)
    
    if 'X' not in b:
        if sum(b) == 0:
            answer = [1, 0]
        elif sum(b) == 4:
            answer = [0, 1]
    return answer

