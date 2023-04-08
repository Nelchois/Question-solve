import sys
from collections import deque
road = []
road_list = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def make_course(N, W):
    if len(road) == N:
        road_list.append(list(road))
        return
    for i in range(W):
        road.append(i)
        make_course(N, W)
        road.pop()

def make_board(H, W, ck_board):
    new_board = [[] for i in range(H)]
    for n in range(W):
        st = ''.join(list(map(str, [ck_board[y][n] for y in range(H)]))).replace('0', '').zfill(H)
        for m in range(H):
            new_board[m].append(int(st[m]))
    return new_board

def make_answer(road_list, ck_board, answer_list):
    print(len(road_list))
    while road_list:
        r = road_list.popleft()
        tu_list = deque()
        broke = 0
        for num in r:
            for h in range(H):
                if ck_board[h][num]:
                    tu_list.append((h, num))
                    break
            while tu_list:
                x, y = tu_list.popleft()
                if not ck_board[x][y]:
                    continue
                broke += 1
                for k in range(4):
                    x_1, y_1 = x, y
                    for _ in range(ck_board[x][y] - 1):
                        x_1 += dx[k]
                        y_1 += dy[k]
                        if 0 <= x_1 < H and 0 <= y_1 < W:
                            tu_list.append((x_1, y_1))
                ck_board[x][y] = 0
                broke += 1
            ck_board = make_board(H, W, ck_board)
        if broke > limit:
            answer_list.append(limit)
        else:
            answer_list.append(broke)
    return

Case = int(sys.stdin.readline())
for _ in range(Case):
    N, W, H = map(int, sys.stdin.readline().split(' '))
    board = list()
    for row in range(H):
        line = tuple(map(int, sys.stdin.readline().split(' ')))
        board.append(line)
    limit = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0:
                limit += 1
    answer_list = []
    ck_board = [list(li) for li in board]
    make_course(N, W)
    make_answer(road_list, ck_board, answer_list)
    print(limit - max(answer_list))

            