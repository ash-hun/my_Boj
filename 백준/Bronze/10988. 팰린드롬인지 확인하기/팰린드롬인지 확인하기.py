s = input()

if len(s)%2 == 0:
    tmp = s[len(s)//2:]
    tmp = tmp[::-1]
    if s[0:len(s)//2] == tmp:
        print(1)
    else:
        print(0)
else:
    tmp = s[len(s)//2+1:]
    tmp = tmp[::-1]
    if s[0:len(s)//2] == tmp:
        print(1)
    else:
        print(0)