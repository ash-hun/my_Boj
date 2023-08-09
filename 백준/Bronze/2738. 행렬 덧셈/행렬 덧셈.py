N, M = map(int, input().split())
Mat = []
for cnt in range(2*N):
    tmp = list(map(int, input().split()))
    if cnt < N:
        Mat.append(tmp)
    else:
        for idx, item in enumerate(tmp):
            Mat[cnt%N][idx] += item

for line in Mat:
    for v in line:
        print(v, end=" ")
    print("")
