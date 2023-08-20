N = int(input())
for step in range(1, N+1):
    if step%2 == 0:
        print(" *"*N)
    else:
        s = "* "*N
        print(s[:-1])