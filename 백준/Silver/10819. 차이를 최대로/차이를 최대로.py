from itertools import permutations

n = int(input())
target_list = list(map(int,input().split())) 

maxV = 0

for i in permutations(target_list):
    tmp = 0
    for j in range(n-1):
        tmp += abs(i[j] - i[j+1])
    maxV = max(maxV,tmp)

print(maxV)