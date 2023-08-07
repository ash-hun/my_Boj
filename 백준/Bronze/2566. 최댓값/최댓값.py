matrix = [list(map(int, input().split())) for _ in range(9)]

maxval = 0
pos = [0,0]
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= maxval:
            maxval = matrix[i][j]
            pos[0], pos[1] = i+1, j+1
print(maxval)
print(pos[0], pos[1])