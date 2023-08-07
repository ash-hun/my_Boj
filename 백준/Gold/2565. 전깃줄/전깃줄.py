if __name__ == "__main__":
    cnt = int(input())
    memo = [0]*cnt # memoization list
    wireB = [] #전봇대 B의 전깃줄 위치
    wireList = [list(map(int, input().split())) for _ in range(cnt)]
    wireList.sort() # 전봇대 A의 전깃줄을 순차정렬

    for i in range(cnt):
        wireB.append(wireList[i][1])

    for i in range(cnt):
        for j in range(i):
            if wireB[i] > wireB[j]:
                if memo[i] < memo[j]:
                    memo[i] = memo[j]
        memo[i] += 1
    
    print(cnt - max(memo))