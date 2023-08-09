case = int(input())
for i in range(case):
    n, S = input().split()
    ans = ""
    for v in S:
        ans += v*int(n)
    print(ans)