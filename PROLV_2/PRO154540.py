#https://school.programmers.co.kr/learn/courses/30/lessons/154540
#Blog post: https://readydeveloperone.blogspot.com/2023/05/154540.html
import sys
sys.setrecursionlimit(10**5)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
island = []
def dfs(maps, now, visit, n, m):
    x, y = now
    k = str(x) + '*' + str(y)
    val = maps[x][y]
    if val == 'X':
        return
    else:
        if k not in visit:
            visit[k] = True
            island[-1] += int(val)
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d] 
                if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                    dfs(maps, [nx, ny], visit, n, m)

def solution(maps):
    answer = []
    visit = dict()
    n, m = len(maps), len(maps[0])
    for x, row in enumerate(maps):
        for y, col in enumerate(row):
            k = str(x) + '*' + str(y)
            if k not in visit:
                visit[k] = True
                if col != 'X':
                    island.append(int(col))
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d] 
                        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                            dfs(maps, [nx, ny], visit, n, m)
                    
    if len(island) == 0:
        return [-1]
    else:
        answer = island
        answer.sort()
    return answer