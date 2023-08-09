N, B = input().split()
target_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N = N[::-1]

res = 0
for idx, i in enumerate(N):
    res += target_list.index(i) * int(B)**idx
print(res)
