array_1 = [list(map(int, input().split())) for _ in range(2)]
array_2 = [list(map(int, input().split())) for _ in range(2)]
for i in range(2):
    print(*[array_1[i][j]*array_2[i][j] for j in range(4)])

