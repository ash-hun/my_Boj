N, M = map(int, input().split())
bucket = [str(item) for item in range(0, N+1)]
for _ in range(1, M+1):
    i, j = map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]
print(" ".join(bucket[1:]))