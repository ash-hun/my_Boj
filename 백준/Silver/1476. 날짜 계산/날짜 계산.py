E, S, M = map(int, input().split())
e,s,m,res = 1,1,1,1

while True:
    if e==E and s==S and m==M:
        break
    e+=1
    s+=1
    m+=1
    res+=1
    if e>15:
        e = e-15
    if s>28:
        s = s-28
    if m>19:
        m = m-19
print(res)