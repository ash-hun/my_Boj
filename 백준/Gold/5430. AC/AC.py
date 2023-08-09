import sys
from collections import deque as dec

T = int(sys.stdin.readline())

for _ in range(T):
    flag = 0
    cmd = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    elements = sys.stdin.readline()[1:-2].split(',')
    target = dec(elements)
    
    if n==0:
        target = []
    
    # if 'D' in cmd and len(elements)==0:
    #     print('error')
    #     continue
    # elif 'R' in cmd and len(elements)==0:
    #     print('error')
    #     continue

    for command in cmd:
        if command == 'R':
            # target.reverse()
            flag += 1
        elif command == 'D':
            if len(target) == 0:
                print('error')
                break
            else:
                if flag%2 == 1:
                    target.pop()
                else:
                    target.popleft()
    else:
        if flag%2 == 1:
            target.reverse()
        print(f'[{",".join(target)}]')