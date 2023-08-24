from collections import deque
import sys

input = sys.stdin.readline

queue = deque()
N = int(input())
for _ in range(N):
    cmd = input()
    if 'push' in cmd:
        command, num = cmd.split()
        queue.append(int(num))
    elif 'pop' in cmd:
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(queue))
    elif 'empty' in cmd:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in cmd:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in cmd:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    # print(*queue)
    