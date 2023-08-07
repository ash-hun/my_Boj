T = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(T):
    x, y = map(int, input().split())

    for row in range(y, y+10):
        for col in range(x, x+10):
            arr[row][col] = 1
tmp = 0
for num in arr:
    tmp += num.count(1)
print(tmp)