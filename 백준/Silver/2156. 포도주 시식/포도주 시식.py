if __name__=="__main__":
    N = int(input())
    wine = [0]
    dp = [0]

    for i in range(N):
        wine.append(int(input()))

    dp.append(wine[1])

    if N>1:
        dp.append(wine[1]+wine[2])

    for j in range(3, N+1):
        dp.append(max(dp[j-1], dp[j-3]+wine[j-1]+wine[j], dp[j-2]+wine[j]))

    print(dp[N])