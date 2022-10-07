
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
maze = []
for i in range(n):
    maze.append(list(sys.stdin.readline().rstrip()))
dx = [1,-1,0,0]
dy = [0,0,-1,1]
maze[0][0] = 1
q = [[0,0]]

while q:
    i, j = q[0][0], q[0][1]
    q.pop(0)
    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if 0 <= x < n and 0 <= y < m and maze[x][y] == '1':
            q.append([x,y])
            maze[x][y] = maze[i][j] + 1
print(maze[n-1][m-1])

                


