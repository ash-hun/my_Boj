a = []
n,m = map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))

b = []
m,k = map(int,input().split())
for i in range(m):
    b.append(list(map(int,input().split())))

res = []
for i in range(n):
    res.append([])
    for j in range(k):
        tmp = 0
        for l in range(m):
            tmp += a[i][l] * b[l][j]
        res[i].append(tmp)

for elem in res:
    print(*elem)