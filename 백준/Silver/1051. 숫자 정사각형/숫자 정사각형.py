def search(board, x, y):
    maxima = min(x, y) # 최대 정사각형 사이즈
    length = 0
    for i in range(x):
        for j in range(y):
            for k in range(maxima):
                if (i+k)<N and (j+k)<M:
                    if (board[i][j] == board[i+k][j+k]) and (board[i][j] == board[i][j+k]) and (board[i][j] == board[i+k][j]):
                        if length < k:
                            length = k
    
    return pow((length+1), 2)

if __name__ == "__main__":
    N, M = map(int, input().split())
    mapping = []
    for _ in range(N):
        s = input()
        s = list(map(int, s))
        mapping.append(s)

    print(search(mapping, N, M))