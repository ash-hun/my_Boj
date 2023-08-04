from itertools import combinations

def filtering(s):
    momo = ['a', 'e', 'i', 'o', 'u']
    mo_cnt, cnt = 0, 0
    for character in s:
        if character in momo:
            mo_cnt += 1
        else:
            cnt += 1
    
    if mo_cnt >= 1 and cnt >= 2:
        return True
    else:
        return False

L, C = map(int, input().split())
target = list(input().split())
res = []
for elem in list(combinations(target, L)):
    tmp = ''.join(sorted(list(elem)))
    if filtering(tmp):
        res.append(tmp)

for target in sorted(res):
    print(target)