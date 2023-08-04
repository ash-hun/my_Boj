from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()

dfs_sol = 0
bfs_sol = 0

visit = [0 for i in range(n+1)]
visit[v] = 1

def bfs(start):
    queue = deque()
    visited = [0 for i in range(n+1)]
    queue.append(start)
    visited[start] = 1

    while len(queue) > 0:
        curr = queue[0]
        print(curr, end=' ')
        for next in graph[curr]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
        queue.popleft()

def dfs(curr):
    print(curr, end=' ')

    for next in graph[curr]:
        if visit[next] == 0:
            visit[next] = 1
            dfs(next)

dfs(v)
print()
bfs(v)