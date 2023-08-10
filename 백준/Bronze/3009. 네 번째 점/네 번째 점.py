if __name__=="__main__":
    x_Set = []
    y_Set = []
    Res_Set = []
    for _ in range(3):
        n, m = map(int, input().split())
        x_Set.append(n)
        y_Set.append(m)
    for i in x_Set:
        if x_Set.count(i) == 1:
            Res_Set.append(i)
            break
    for i in y_Set:
        if y_Set.count(i) == 1:
            Res_Set.append(i)
            break
    print(Res_Set[0], Res_Set[1])