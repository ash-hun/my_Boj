import math as M

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(' ')
    else:
        while(N != 1):
            for i in range(2, N+1):
                if N%i == 0:
                    print(i)
                    N //= i
                    break