val = []
for i in range(int(input())):
    tmp = int(input())
    val.append(tmp)

val.sort()
for i in range(len(val)):
    print(val[i])