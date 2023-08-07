uniqueNum = list(map(int, input().split()))
for i in range(len(uniqueNum)):
    uniqueNum[i] = uniqueNum[i]**2
print(sum(uniqueNum)%10)