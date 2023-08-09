N = int(input())
for _ in range(N):
    res = []
    M = int(input())
    for i in [25, 10, 5, 1]:
        res.append(M//i)
        M = M%i
    print(*res)