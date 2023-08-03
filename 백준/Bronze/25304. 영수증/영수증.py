target = int(input())
cnt = int(input())
tmp = 0
for _ in range(cnt):
    price, count = input().split()
    tmp += int(price)*int(count)
if tmp == target:
    print("Yes")
else:
    print("No")