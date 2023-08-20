import sys

if __name__=='__main__':
    N = int(sys.stdin.readline())
    value = [0 for _ in range(10001)]

    for i in range(N):
        res = int(sys.stdin.readline())
        value[res] += 1
    
    for j in range(len(value)):
        for k in range(value[j]):
            print(j)