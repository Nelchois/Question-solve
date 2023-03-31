#https://school.programmers.co.kr/learn/courses/30/lessons/160585
def winner(marker_list):
    if len(marker_list) < 3:
        return False
    for row in range(3):
        row_list = [row == mark[0] for mark in marker_list]
        if row_list.count(True) >= 3:
            return True
    for col in range(3):
        col_list = [col == mark[1] for mark in marker_list]
        if col_list.count(True) >= 3:
            return True
    if (1, 1) in marker_list:
        if (2, 2) in marker_list and (0, 0) in marker_list:
            return True
        if (2, 0) in marker_list and (0, 2) in marker_list:
            return True
    return False

def solution(board):
    answer = 1
    marker = ['O', 'X']
    board_dic = {'O': [], 'X': []}
    cnt = [0] * 2
    for i in range(3):
        row = board[i]
        for j in range(3):
            marker = row[j]
            if marker == 'O':
                cnt[0] += 1
                board_dic['O'].append((i, j))
            elif marker == 'X':
                cnt[1] += 1
                board_dic['X'].append((i, j))
    Ogame = winner(board_dic['O'])
    Xgame = winner(board_dic['X'])
    if sum(cnt) == 0:
        return answer
    if (cnt[0] < cnt[1]) or (abs(cnt[0] - cnt[1]) >= 2):
        answer = 0
        return answer
    if Ogame == True and Ogame == Xgame:
        answer = 0
        return answer
    if Ogame == True:
        if cnt[0] != cnt[1] + 1:
            answer = 0
            return answer
    if Xgame == True:
        if cnt[0] != cnt[1]:
            answer = 0
            return answer
    return answer