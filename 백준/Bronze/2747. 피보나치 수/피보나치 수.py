fibo = lambda n, a=0, b=1 : a if n <= 0 else fibo(n-1, b, a+b)
n = int(input())
print(fibo(n))