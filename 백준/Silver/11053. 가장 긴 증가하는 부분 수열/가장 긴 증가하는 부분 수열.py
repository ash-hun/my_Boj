N = int(input())
A = list(map(int, input().split()))
ch = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            ch[i] = max(ch[i], ch[j]+1)

print(max(ch))