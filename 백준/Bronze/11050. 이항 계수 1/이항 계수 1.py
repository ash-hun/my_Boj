def binomial(n, k):
    if k==n or k ==0:
        return 1
    else:
        return binomial(n-1, k-1) + binomial(n-1, k)

N, K = map(int, input().split())
print(binomial(N, K))