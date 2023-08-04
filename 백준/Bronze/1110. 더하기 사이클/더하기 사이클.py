N = int(input())
origin = N
new = 0
tmp = 0
cnt = 0
while True:
    tmp = N//10 + N%10
    new = (N%10)*10 + tmp%10
    cnt += 1
    N = new
    if origin == new:
        break
        
print(cnt)  