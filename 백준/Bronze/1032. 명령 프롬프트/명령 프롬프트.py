n = int(input())
a = list(input())
l = len(a)
for _ in range(n-1):
    b = list(input())
    for i in range(l):
        if a[i] != b[i]:
            a[i] = '?'
print(''.join(a))