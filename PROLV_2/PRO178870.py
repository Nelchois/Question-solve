#https://school.programmers.co.kr/learn/courses/30/lessons/178870
from collections import deque
def solution(sequence, k):
    ans = []
    board = deque()
    idx_list = deque()
    sum_num = 0
    for idx, num in enumerate(sequence):
        board.append(num)
        idx_list.append(idx)
        sum_num += num
        while sum_num > k and len(board) >= 1:
            out = board.popleft()
            idx_list.popleft()
            sum_num -= out
        if sum_num == k:
            if len(ans) == 0:
                ans = tuple(idx_list)
            elif len(ans) > 0:
                if len(ans) > len(idx_list):
                    ans = tuple(idx_list)
    return [ans[0], ans[-1]]