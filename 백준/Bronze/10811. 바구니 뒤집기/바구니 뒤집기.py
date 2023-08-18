N, M = map(int, input().split())

bucket = [i for i in range(1,N+1)]

for i in range(M):
    i,j = map(int, input().split())
    tmp = bucket[i-1:j]
    tmp.reverse()
    bucket[i-1:j] = tmp

for i in range(N):
    print(bucket[i], end = ' ')