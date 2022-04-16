chess_line = list(input() for _ in range(8))
count = 0
for i in range(8):
    for j in range(8):
        if i == 0 or i%2 == 0:
            if j == 0 or j%2 == 0:
                if chess_line[i][j] == 'F':
                    count +=1
        elif i != 0 and i%2 !=0:
            if j != 0 and j%2 != 0:
                if chess_line[i][j] == 'F':
                    count +=1
print(count)

