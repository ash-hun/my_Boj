s = list(input())
tmp = ""
for idx, elem in enumerate(s):
    if idx%10 == 9:
        tmp += elem
        print(tmp)
        tmp = ""
    else:
        tmp += elem
else:
    print(tmp)