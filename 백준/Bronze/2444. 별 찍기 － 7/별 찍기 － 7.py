N = int(input())
for upperLine in range(N):
    print(" "*(N-upperLine-1) + "*"*(2*upperLine+1))
for underLine in range(N-1,0,-1):
    print(" "*(N-underLine) + "*"*(2*underLine-1))