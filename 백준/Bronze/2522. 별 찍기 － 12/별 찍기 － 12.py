N = int(input())

for upperLine in range(1, N+1):
    print(' '*(N-upperLine) + '*'*upperLine)
for underLine in range(1, N):
    print(' '*underLine + '*'*(N-underLine))