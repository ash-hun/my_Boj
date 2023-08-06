from itertools import combinations as cc
import copy

hobit = [int(input()) for _ in range(9)]
pick = list(cc(hobit, 2))
tmp = copy.deepcopy(hobit)
for i in range(len(pick)):
    tmp.remove(pick[i][0])
    tmp.remove(pick[i][1])
    if sum(tmp) == 100:
        break
    else:
        tmp = copy.deepcopy(hobit)

tmp.sort()
for elem in tmp:
    print(elem)