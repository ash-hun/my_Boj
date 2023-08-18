T = int(input())

for i in range(T):
    h, w, n = map(int, input().split())
    room = n//h+1
    floor = n%h
    if floor==0:
        floor=h
        room-=1
    print(floor*100+room)