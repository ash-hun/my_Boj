N, K = map(int, input().split())
dp = [[0,0]]
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    W, V = map(int, input().split())
    dp.append([W,V])
    
for i in range(1, N+1):
    for j in range(1, K+1):
        if j>= dp[i][0]:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-dp[i][0]]+dp[i][1])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][K])