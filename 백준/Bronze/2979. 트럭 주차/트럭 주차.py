a, b, c = map(int, input().split())
ans, arr = 0, [0]*100

board = {0:0, 1:a, 2:b*2, 3:c*3}
for _ in range(3):
    begin, end = map(int, input().split())
    for i in range(begin, end):
        arr[i] += 1
for j in arr:
    ans += board[j]
print(ans)