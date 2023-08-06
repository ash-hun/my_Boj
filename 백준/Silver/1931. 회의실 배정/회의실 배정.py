N = int(input())
waitlist = []

for _ in range(N):
    waitlist.append(list(map(int, input().split())))

waitlist.sort(key=lambda x: (x[1],x[0]))
nowEnd = 0
ans = 0

for s, e in waitlist:
    if s >= nowEnd:
        nowEnd = e
        ans +=1
print(ans)