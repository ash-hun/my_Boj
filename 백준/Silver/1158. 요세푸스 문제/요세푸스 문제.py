N, K = map(int,input().split())
res, target = [], 0
useList = [elem for elem in range(1,N+1)] 

for i in range(N):
    target+=(K-1)
    if target >= len(useList):
        target %= len(useList)
    res.append(str(useList[target]))
    useList.pop(target)

print("<",', '.join(res),">", sep="")