currentList = list(map(int, input().split()))
originList = [1,1,2,2,2,8]
ans = ""
for idx in range(0, len(currentList)):
    ans += str(originList[idx]-currentList[idx])+" "
print(ans)