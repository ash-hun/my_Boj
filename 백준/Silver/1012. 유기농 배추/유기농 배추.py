from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >=M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for _ in range(T):
    bug = 0
    M, N, k = map(int,input().split())
    graph = [[0]*N for _ in range(M)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for xPos in range(M):
        for yPos in range(N):
            if graph[xPos][yPos] == 1:
                bfs(graph, xPos, yPos)
                bug += 1
    print(bug)