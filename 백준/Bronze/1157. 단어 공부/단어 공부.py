word = input().upper()
S = list(set(word))
cnt = []

for v in S:
    cnt.append(word.count(v))

if cnt.count(max(cnt))>=2:
    print('?')
else:
    print(S[(cnt.index(max(cnt)))])
