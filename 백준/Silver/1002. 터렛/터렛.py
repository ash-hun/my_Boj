import math
T = int(input())

for _ in range(T):
    tmp = []
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    distance = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r_1 == r_2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r_1-r_2) == distance or r_1 + r_2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r_1-r_2) < distance < (r_1+r_2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에