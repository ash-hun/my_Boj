from itertools import permutations
N = int(input())

useList = [str(item) for item in range(1, 10)]
allCase = list(permutations(useList, 3))

for _ in range(N):
    target, s, b = map(int, input().split())
    target = list(str(target))
    cnt = 0

    for i in range(len(allCase)):
        strike = ball = 0
        i -= cnt
        for j in range(3):
            if allCase[i][j] == target[j]:
                strike += 1
            elif target[j] in allCase[i]:
                ball += 1
        
        if strike != s or ball != b:
            allCase.remove(allCase[i])
            cnt += 1
print(len(allCase))