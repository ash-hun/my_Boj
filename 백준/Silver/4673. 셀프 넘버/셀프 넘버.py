def d(n):
    res = n
    for num in list(str(n)):
        res += int(num)
    return res

Number = []
for cnt in range(10001):
    Number.append(d(cnt))
Number.sort()
for cnt in range(1, 10000):
    if cnt in Number:
        continue
    else:
        print(cnt)