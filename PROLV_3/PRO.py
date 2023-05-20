dX = [(1, 0), (0, 1), (0, -1), (-1, 0)]
island = []
def dfs(maps, now, visit, n, m):
    nx, ny = now
    for i in range(4):
        dx, dy = dX[i]
        x, y = nx + dx, ny + dy
        #if 0 <= x <= len(maps) - 1 and 0 <= y <= m - 1:
        if 0 <= x <= n - 1 and 0 <= y <= m - 1:
            k = str(x) + '*' + str(y)
            if k not in visit:
                visit[k] = True
                val = maps[x][y]
                if val != 'X':
                    island[-1] += int(val)
                    dfs(maps, (x, y), visit, n, m)

def solution(maps):
    answer = []
    visit = dict()
    n, m = len(maps), len(maps[0])
    for x, row in enumerate(maps):
        for y, col in enumerate(row):
            now = (x, y)
            k = str(x) + '*' + str(y)
            if k not in visit:
                visit[k] = True
                if col != 'X':
                    island.append(int(col))
                    dfs(maps, now, visit, n, m)
    if len(island) == 0:
        return [-1]
    else:
        answer = island
        answer.sort()
    return answer