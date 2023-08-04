from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())
info = []
for _ in range(L):
    t, d = map(str, input().split())
    info.append((int(t), d))
    
dx = [0, 1, 0, -1] #아래, 위, 왼, 오
dy = [1, 0, -1, 0]

now_d, curr_x, curr_y = 0, 0, 0
time_step, i = 0, 0
queue = deque() # 뱀 위치 아오
queue.append((curr_x, curr_y))

while 1:
    curr_x = curr_x + dx[now_d]
    curr_y = curr_y + dy[now_d]
    time_step += 1
    if curr_x < 0 or curr_x >= N or curr_y < 0 or curr_y >= N or (curr_x, curr_y) in queue:
        break
    queue.append((curr_x, curr_y))
    if board[curr_x][curr_y] == 0:
        queue.popleft()
    else:
        board[curr_x][curr_y] = 0
    if time_step == info[i][0]:
        if info[i][1] == 'L':
            now_d = (now_d - 1)%4
        else:
            now_d = (now_d + 1)%4
        if i + 1 < len(info):   i += 1
    # print(queue)

print(time_step)