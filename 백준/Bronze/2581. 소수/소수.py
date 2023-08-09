import math as m

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(m.sqrt(num)+1)):
        if num%i == 0:
            return 0
    return 1

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    res = []
    for j in range(M, N+1):
        if isPrime(j):
            res.append(j)
    
    if len(res)==0:
        print('-1')
    else:
        print(sum(res))
        print(min(res))