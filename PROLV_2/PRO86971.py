#https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque
def solution(n, wires):
    answer = -1
    maps = dict()
    for li in wires:
        v1, v2 = li
        if str(v1) not in maps:
            maps[str(v1)] = [v2]
        else:
            maps[str(v1)].append(v2)
        if str(v2) not in maps:
            maps[str(v2)] = [v1]
        else:
            maps[str(v2)].append(v1)
    ans_list = set()
    for cut in wires:
        c1, c2 = cut
        visit = dict()
        for i in range(1, n + 1):
            que = deque()
            if str(i) in visit:
                continue
            else:
                que.append(i)
                visit[str(i)] = True
                while que:
                    le = que.popleft()
                    for num in maps[str(le)]:
                        if (le == c1 and num == c2) or (le == c2 and num == c1):
                            continue
                        if str(num) not in visit:
                            que.append(num)
                            visit[str(num)] = True
                ans_list.add(abs(len(visit) - (n - len(visit))))
                break
    answer = min(list(ans_list))
            
    return answer