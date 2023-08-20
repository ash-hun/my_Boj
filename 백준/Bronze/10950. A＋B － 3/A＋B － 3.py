N = int(input())
res =[]
for i in range(N):
    a, b = input().split()
    res.append(int(a)+int(b))

for i in range(N):
    print(res[i])