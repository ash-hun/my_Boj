from collections import deque

n, l, r = map(int, input().split())
worldmap = [list(map(int, input().split())) for _ in range(n)]

day, isOpen = 0, False

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i, j):
    queue = deque()
    unionCountry = []
    queue.append((i, j))
    unionCountry.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nxt_x = x + dx[k]
            nxt_y = y + dy[k]
            if 0 <= nxt_x < n and 0 <= nxt_y < n and visited[nxt_x][nxt_y] == 0:
                if l <= abs(worldmap[nxt_x][nxt_y]-worldmap[x][y]) <= r:
                    visited[nxt_x][nxt_y] = 1
                    queue.append((nxt_x, nxt_y))
                    unionCountry.append((nxt_x, nxt_y))
    return unionCountry

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if visited[row][col] == 0:
                visited[row][col] = 1
                country = bfs(row, col)
                
                if len(country) > 1:
                    isOpen = True
                    population = sum(worldmap[xIdx][yIdx] for xIdx, yIdx in country) // len(country)
                    
                    for xIdx, yIdx in country:
                        worldmap[xIdx][yIdx] = population
    
    if isOpen == False:
        print(day)
        break

    isOpen = False
    day += 1