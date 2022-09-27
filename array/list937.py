array_1 = [list(map(int, input().split())) for _ in range(2)]
array_2 = [list(map(int, input().split())) for _ in range(2)]
total_list = []
for i in range(2):
    total_list.append([array_1[i][j]*array_2[i][j] for j in range(3)])
print(*total_list[0])
print(*total_list[1])
