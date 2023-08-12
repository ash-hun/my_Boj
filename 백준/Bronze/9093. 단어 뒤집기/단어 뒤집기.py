T = int(input())
S = [list(input().split()) for i in range(T)]

for i in range(T):
    for j in S[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()