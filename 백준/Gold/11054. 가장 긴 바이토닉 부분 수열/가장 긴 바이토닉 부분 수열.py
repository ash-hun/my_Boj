import sys
N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
count1 = [0 for _ in range(N)]
count2 = [0 for _ in range(N)]
for i in range(N):
        for j in range(i):
            if arr[i]>arr[j] :
                if count1[i]<count1[j]:
                    count1[i] = count1[j]
        count1[i]+=1
arr.reverse()
for i in range(N):
        for j in range(i):
            if arr[i]>arr[j] :
                if count2[i]<count2[j]:
                    count2[i] = count2[j]
        count2[i]+=1
M = 0

for i in range(N):
    if count1[i]+count2[N-i-1]-1 >M:
        M = count1[i]+count2[N-i-1]-1

print(M)