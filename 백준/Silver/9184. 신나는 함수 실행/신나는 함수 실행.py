arr = [[[ None for _ in range(101)] for _ in range(101)] for _ in range(101)]
def w(a,b,c):
    if arr[a][b][c]:
        return arr[a][b][c]

    if a <= 50 or b <= 50 or c <= 50:
        arr[a][b][c] = 1
        return 1

    if a > 70 or b > 70 or c > 70:
        arr[a][b][c]= w(70,70,70)
        return arr[a][b][c]

    if a < b and b < c:
        if arr[a][b][c-1] == None:
            arr[a][b][c-1] = w(a,b,c-1)
        if arr[a][b-1][c-1] == None:
            arr[a][b-1][c-1] = w(a,b-1,c-1)
        if arr[a][b-1][c] == None:
            arr[a][b-1][c] = w(a,b-1,c)

        return arr[a][b][c-1] + arr[a][b-1][c-1] - arr[a][b-1][c]

    if arr[a-1][b][c]==None:
        arr[a-1][b][c] = w(a-1,b,c)
    if arr[a-1][b-1][c]==None:
        arr[a-1][b-1][c] = w(a-1,b-1,c)
    if arr[a-1][b][c-1]==None:
        arr[a-1][b][c-1] = w(a-1,b,c-1)
    if arr[a-1][b-1][c-1]==None:
        arr[a-1][b-1][c-1] = w(a-1,b-1,c-1)
    return arr[a-1][b][c] + arr[a-1][b-1][c] + arr[a-1][b][c-1] - arr[a-1][b-1][c-1]

while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) ="%(a,b,c),w(a+50,b+50,c+50))