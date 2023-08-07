N = int(input())

for upperLine in range(1, N+1):
    print(" " * (upperLine-1) + "*" * (2 * (N-upperLine) + 1))
for underLine in range(1, N):
    print(" " * (N-underLine-1) + "*" * (2*underLine + 1))