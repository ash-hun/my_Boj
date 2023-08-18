note, maxlen = [], 0
ans = ""
for i in range(5):
    s = list(input())
    if maxlen < len(s):
        maxlen = len(s)
    note.append(s)

for line in note:
    if len(line) != maxlen:
        tmp = ["@"]*(maxlen-len(line))
        line.extend(tmp)

for i in range(maxlen):
    for j in range(5):
        ans += note[j][i]

print(ans.replace("@", ""))
