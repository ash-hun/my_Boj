def fibo(n):
    tmp1, tmp2 = 0, 1
    if n == 1:
        return 1
    k = abs(n)
    for _ in range(k):
        tmp1, tmp2 = tmp2, (tmp1+tmp2)%1000000000
    return tmp1

if __name__ == '__main__':
    n = int(input())
    res = 0
    if n>=0:
        if n==0:
            print(0)
        else:
            print(1)
        print(fibo(n))
    else:
        if abs(n)%2==0:
            print(-1)
        else:
            print(1)
        print(fibo(n))