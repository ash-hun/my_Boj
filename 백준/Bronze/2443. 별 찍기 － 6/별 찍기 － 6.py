N = int(input())

for line in range(N, 0, -1):
    print(" "*(N-line)+"*"*(2*line-1))