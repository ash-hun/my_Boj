if __name__=="__main__":
    N = int(input())
    res = 0
    for i in range(1, N+1):
        create = map(int, str(i))
        res = i + sum(create)
        if res == N:
            print(i)
            break

        if i == N:
            print(0)