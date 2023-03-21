#https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer_list = []
board = []
def make_route(dungeons, visit, k):
    if len(board) == len(dungeons):
        ck_num = k
        cnt = 0
        for order in board:
            now = dungeons[order]
            if ck_num < now[0]:
                answer_list.append(cnt)
                return
            else:
                ck_num -= now[1]
                if ck_num < 0:
                    answer_list.append(cnt)
                    return
                cnt += 1
        answer_list.append(cnt)
        return
    for i in range(len(dungeons)):
        if visit[i] == 0:
            visit[i] = 1
            board.append(i)
            make_route(dungeons, visit, k)
            board.pop()
            visit[i] = 0
            
def solution(k, dungeons):
    visit = [0 for i in range(len(dungeons))]
    make_route(dungeons, visit, k)
    answer = -1
    if len(answer_list) > 0:
        answer = max(answer_list)
    return answer