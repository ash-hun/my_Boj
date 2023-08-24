N = int(input())

dp = [0 for i in range(N+1)]
calendar = [list(map(int, input().split())) for _ in range(N)] # 소요시간, 가격

for day in range(N):
    for cost in range(day + calendar[day][0], N+1):
        if dp[cost] < dp[day]+calendar[day][1]:
            dp[cost] = dp[day] + calendar[day][1]

print(dp[-1])