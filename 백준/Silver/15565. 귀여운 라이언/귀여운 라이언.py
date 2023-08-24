N,K = map(int, input().split())
arr = input().split()

if arr.count('1') < K :
    print(-1)
else:
    lion = [i for i, x in enumerate( arr ) if x == '1']
    print(min(lion[K-1+j] - lion[j] + 1 for j in range(len(lion)-K+1)))