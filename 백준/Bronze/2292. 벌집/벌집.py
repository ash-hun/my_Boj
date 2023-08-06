n = int(input())
tmp = 1
while n>1:
    n -= (6*tmp)
    tmp += 1
print(tmp)