#https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque
def solution(begin, target, words):
    ans_list = []
    num = len(begin)
    if target not in words:
        return 0
    idx_list = [0] * len(words)
    q = deque()
    q.append([begin, 0])
    while q:
        last_w, count = q.popleft()
        if last_w == target:
            ans_list.append(count)
        for i in range(len(words)):
            dif = 0
            for _ in range(num):
                if words[i][_] != last_w[_]:
                    dif += 1
            if dif == 1 and idx_list[i] == 0:
                idx_list[i] = 1
                q.append([words[i], count+1])
    answer = min(ans_list)
    return answer
