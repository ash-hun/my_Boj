N = int(input())
for upperLine in range(1,N+1):
    print(('*'*upperLine) + ' '*(N-upperLine) + ' '*(N-upperLine) + ('*'*upperLine))
for underLine in range(N-1, 0, -1):
    print('*'*(underLine) + ' '*(N-underLine)+' '*(N-underLine)+'*'*(underLine))