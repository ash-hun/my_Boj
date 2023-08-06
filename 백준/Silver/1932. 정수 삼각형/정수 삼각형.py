import sys

N = int(sys.stdin.readline())
tri = [list(map(int,sys.stdin.readline().split())) for _ in range(0,N)]

for i in range(1,N):
    for j in range(len(tri[i])):
        if j == 0 : 
            tri[i][j] += (tri[i-1][j])
        elif j==i:
            tri[i][j] +=(tri[i-1][j-1])
        else :
            tri[i][j] += (max(tri[i-1][j],tri[i-1][j-1]))
print(max(tri[N-1]))
