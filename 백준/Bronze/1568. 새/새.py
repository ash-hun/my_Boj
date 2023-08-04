N = int(input())
cnt,i = 0,1
while N>0:
    if i > N:
        i = 1
        continue
    cnt += 1
    N -= i
    i += 1
print(cnt)