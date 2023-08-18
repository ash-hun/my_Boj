# f(n) = f(n-1) + f(n-2) + f(n-3) (n>=4) {f(1)=1,f(2)=2,f(3)=4}
T = int(input())

for _ in range(T) :
    N = int(input())
    dp = [0]*(N+1)
    if N == 1 :
        print(1)
    elif N == 2 :
        print(2)
    elif N == 3 :
        print(4)
    else :
        dp[1], dp[2], dp[3] = 1, 2, 4
        for j in range(4,N+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        # print(dp)
        # print()
        print(dp[N])