black_num = int(input())
paper = list([0 for i in range(100)] for _ in range(100))
sum = 0
for _ in range(black_num):
    x_number, y_number = map(int,input().split())
    for i in range(0,10):
        for j in range(0,10):
            if paper[(99-y_number)-i][x_number+j] == 0:
                paper[(99-y_number)-i][x_number+j] =1
                sum += 1
            if paper[(99-y_number)-i][x_number+j] != 1:
                continue
print(sum)
