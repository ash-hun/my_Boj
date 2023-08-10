T = int(input())
for _ in range(T):
    k = int(input())#층
    n = int(input())#호
    room = [k for k in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            room[j] += room[j-1]
            #print("{0}층 {1}번째 : {2}, ".format(i+1, j+1, room[j]))
    print(room[-1])
