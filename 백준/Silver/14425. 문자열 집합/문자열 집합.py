N, M = map(int, input().split())
S = set()
cnt = 0
for _ in range(N):
    s = input()
    S.add(s)
for _ in range(M):
    s = input()
    if s in S:
        cnt += 1
print(cnt)
