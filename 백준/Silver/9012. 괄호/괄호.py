def is_VPS(data):
    sum = 0
    for i in data:
        if i =='(':
            sum += 1
        elif i ==')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
        
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")

Case = int(input())

for i in range(Case):
    S = list(input())
    is_VPS(S)