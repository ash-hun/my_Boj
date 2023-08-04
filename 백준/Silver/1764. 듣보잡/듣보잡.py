N, M = map(int, input().split())
noListen = set([input() for _ in range(N)])
noSee = set([input() for _ in range(M)])
res = list(noListen & noSee)

res.sort()
print(len(res))
for elem in res:
    print(elem)