n, k = map(int, input().split())
m = []
number = 0
for _ in range(n):
    m.append(int(input()))

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        continue
    number += k // m[i]
    k %= m[i]
print(number)