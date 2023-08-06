#<--- BOJ 1929번 --->
# Siver 2, Prime Number
# Prime Number = 1과 자기자신으로밖에 나누어 떨어지지 않는 수
import math as m

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(m.sqrt(num)+1)):
        if num%i == 0:
            return 0
    return 1

if __name__ == "__main__":
    M, N = map(int, input().split())

    for j in range(M, N+1):
        if isPrime(j):
            print(j)