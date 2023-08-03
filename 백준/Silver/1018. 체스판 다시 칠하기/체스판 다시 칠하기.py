N, M = map(int, input().split())

chess = [input() for i in range(N)]
min_count = 2501 # n, m의 최댓값의 곱 +1

for i in range(N-7):
    for j in range(M-7):
        count1, count2 = 0, 0 #count1 => B의 개수, count2 => W의 개수
        for row in range(i, i+8):
            for col in range(j, j+8):
                # (row + col)이 짝수이면 처음과 같은 색, 왜? 0,0의 색이 기준이니까
                if (row+col) % 2:
                    if chess[row][col] != 'W':
                        count1 += 1
                    if chess[row][col] != 'B':
                        count2 += 1
                else:
                    if chess[row][col] != 'B':
                        count1 += 1
                    if chess[row][col] != 'W':
                        count2 += 1
                        
        if min_count > count1:
            min_count = count1
        if min_count > count2:
            min_count = count2
        # min_count = min(count1, count2)
print(min_count)

# 1. 입력받아 맵을 만든다.
# 2. 정답 맵을 만든다.
# 3. 각 요소에 대해 xor연산을 수행하여 결과를 저장한다.
# 4. 3의 결과의 총합을 구한다.
# 5. 이러면 다른방식으로 구할 수 있지 않을까? ^^
# T = {'W':1, 'B':0}
# A = ['W', 'B']
# B = ['B', 'W']
# for a, b in zip(A, B):
#     print(T[a]^T[b])
# res
# 1
# 1