n,m = map(int, input().split())

bucket = ["0"]*(n+1)
for cnt in range(0, m):
    i, j, k = input().split()
    for idx in range(int(i), int(j)+1):
        bucket[idx] = k
print(" ".join(bucket[1:]))
