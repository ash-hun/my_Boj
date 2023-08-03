N = int(input())
res = []
tmp = []
cnt = 0
for i in range(N):
    s = input()
    if s == 'ENTER':
        res.append(list(set(tmp)))
        tmp = []
    else:
        tmp.append(s)
cnt += len(list(set(tmp)))
for elem in res:
    cnt += len(elem)
print(cnt)