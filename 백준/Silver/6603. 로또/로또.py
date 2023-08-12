from itertools import combinations as C
while True:
    k, *s = map(int, input().split())
    if k != 0:
        for elem in list(C(s, 6)):
            print(*elem)
        print()
    else:
        break