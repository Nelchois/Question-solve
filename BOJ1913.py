input_number = int(input())
Size_number = input_number*input_number
Max_input = Size_number
Cell_list = [[0 for _ in range(input_number)] for __ in range(Size_number)]
for i in range(Size_number):
    for j in range(Size_number):
        if j < input_number and i == 0:
            if Cell_list[j][i] == 0:
                Cell_list[j][i] = (Max_input -j)
        elif j >=input_number and i < input_number:
            if Cell_list[j][i] == 0:
                Cell_list[j][i] = (Max_input -j)     
        

'''
n = int(input())
find_number = int(input())
board = [[0] * n for _ in range(n)]

x, y = 0, 0
direction = 0
# 아래, 오른, 위, 왼
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(n * n, 0, -1):
    if i == find_number:
        find_x, find_y = x + 1, y + 1

    board[x][y] = i
    dx, dy = dxy[direction]
    nx, ny = x + dx, y + dy

    # 1. 정상 범위
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
    # 2. 인덱스를 벗어나거나, 다른 숫자 있음
    else:
        direction = (direction + 1) % 4
        dx, dy = dxy[direction]
        nx, ny = x + dx, y + dy
        x, y = nx, ny

# 전체 표 출력
for line in board:
    for number in line:
        print(number, end=" ")
    print()

# 찾는 숫자의 좌표 출력
print(find_x, find_y)
'''