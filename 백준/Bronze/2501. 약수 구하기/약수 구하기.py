p, q = map(int, input().split())

tmp = []
for i in range(1, p+1):
    if p%i == 0:
        tmp.append(i)

if len(tmp)<q:
    print(0)
else:
    print(tmp[q-1])
