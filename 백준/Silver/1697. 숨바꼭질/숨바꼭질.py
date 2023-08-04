from collections import deque

maxval = 100000
n,k = map(int,input().split())
distance = [0] * (maxval+1)


q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(distance[x])
        break
    
    moveRange = [x-1,x+1,2*x]
    for movePos in moveRange:
        if 0<= movePos <= maxval and not distance[movePos]:
            distance[movePos] = distance[x] +1
            q.append(movePos)