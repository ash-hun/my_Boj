h, m = map(int, input().split())
proceed = int(input())

if m+proceed >= 60:
    h += (m+proceed)//60
    m = (m+proceed)%60
    if h>=24:
        h-=24
else:
    m += proceed
    
print(f"{h} {m}")