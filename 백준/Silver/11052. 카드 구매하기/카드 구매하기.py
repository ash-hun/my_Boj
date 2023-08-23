# dp[i] = 카드 i개 구매하는 최대 가격 , p[k] = k개가 들어있는 카드팩 가격
# dp[i] = p[k] + dp[i - k]
N = int(input())
pack = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for k in range(1,i+1):
        target_i = dp[i]
        each_case_sum = dp[i-k]+pack[k]
        dp[i] = max(target_i, each_case_sum)
print(dp[i])