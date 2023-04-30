#https://school.programmers.co.kr/learn/courses/30/lessons/64064
board = []
ans = set()
def make(idx, banned_id, visit, possible):
    if len(board) == len(banned_id):
        a = tuple(sorted(board))
        ans.add(a)
        return
    key = banned_id[idx]
    se = possible[key]
    for i in se:
        if visit[i] == 0:
            board.append(i)
            visit[i] = 1
            if idx < len(banned_id):
                make(idx+1, banned_id, visit, possible)
            board.pop()
            visit[i] = 0
    
def solution(user_id, banned_id):
    answer = 0
    same = []
    possible = dict()
    for ban in banned_id:
        for p in range(len(user_id)):
            user = user_id[p]
            if len(ban) == len(user):
                ck = True
                for i in range(len(ban)):
                    if ban[i] == '*':
                        continue
                    else:
                        if ban[i] != user[i]:
                            ck = False
                            break
                if ck == True:
                    if ban not in possible:
                        possible[ban] = set()
                        possible[ban].add(p)
                    else:
                        possible[ban].add(p)
    visit = [0] * len(user_id)
    make(0, banned_id, visit, possible)
    answer = len(ans)
    return answer