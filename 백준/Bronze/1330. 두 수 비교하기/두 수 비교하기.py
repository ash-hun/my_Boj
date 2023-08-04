#--------------------------------
# Boj 1330 (Bronze 4)
#--------------------------------
A, B = map(int, input().split())

if A == B:
    print("==")
else:
    print(">") if A > B else print("<")