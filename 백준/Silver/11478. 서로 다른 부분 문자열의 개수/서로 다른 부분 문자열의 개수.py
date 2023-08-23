s = input()
ans = []
for idx in range(len(s)):
    for subidx in range(idx, len(s)):
        ans.append(s[idx:subidx+1])

print(len(set(ans)))
