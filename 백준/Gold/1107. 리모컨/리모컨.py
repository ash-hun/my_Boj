N = int(input())
M = int(input())
if M != 0:
    M_List = list(input().split())
else:
    M_List = []
ans = abs(100 - N)

for channel in range(1000001):
    for btn in str(channel):
        if btn in M_List:
            break
    else:
        ans = min(ans, len(str(channel)) + abs(channel - N))

print(ans)