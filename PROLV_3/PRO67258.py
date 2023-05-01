#https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import deque, Counter
def solution(gems):
    category = set(gems)
    gem = dict()
    for idx, g in enumerate(gems):
        gem[f'{idx + 1}'] = g
    c = Counter()
    st = 1
    ans_list = []
    for i in range(len(gems)):
        c[gem[str(i+1)]] += 1
        while True:
            if len(c) != len(category):
                break
            c[gem[str(st)]] -= 1
            if c[gem[str(st)]] == 0:
                del c[gem[str(st)]]
            ans_list.append([st, i+1])
            st += 1
    ans_list.sort(key = lambda x: (x[1] - x[0], x[1]))
    answer = ans_list[0]
    return answer