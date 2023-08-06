import math as m

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(m.sqrt(num)+1)):
        if num%i == 0:
            return 0
    return 1

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    res = []
    for j in range(len(num)):
        if isPrime(num[j]):
            res.append(num[j])
    
    print(len(res))