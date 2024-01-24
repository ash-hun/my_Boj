from collections import Counter as C

N = int(input())
N_cards = list(map(int, input().split()))
M = int(input())
M_cards = list(map(int, input().split()))

cnts = dict(C(N_cards))

for target in M_cards:
    result = cnts.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")