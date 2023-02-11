#https://school.programmers.co.kr/learn/courses/30/lessons/92341
def solution(fees, records):
    board = dict()
    answer = []
    basic_time = fees[0]
    basic_charge = fees[1]
    extra_time = fees[2]
    extra_charge = fees[3]
    for i in records:
        car_num = i[6:10]
        time = int(i[0:5][0:2]) * 60 + int(i[0:5][3:5])
        if i[-1] == 'N':
            if car_num not in board:
                board[car_num] = [time, basic_charge, 0, True]
            else:
                board[car_num][0] = time
                board[car_num][3] = True
        elif i[-1] == 'T':
            use = time - board[car_num][0]
            board[car_num][2] += use 
            board[car_num][3] = False
    for j in board:
        if board[j][3] == True:
            use = 1439 - board[j][0] + board[j][2] - basic_time
            if use > 0:
                if use % extra_time == 0:
                    board[j][1] += use//extra_time * extra_charge
                else:
                    board[j][1] += (use//extra_time + 1) * extra_charge
        else:
            use = board[j][2] - basic_time
            if use > 0:
                if use % extra_time == 0:
                    board[j][1] += use//extra_time * extra_charge
                else:
                    board[j][1] += (use//extra_time + 1) * extra_charge
    for i in sorted(board):
        answer.append(board[i][1])
    return answer