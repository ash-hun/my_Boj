N = int(input())
target_num = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 북, 동, 남, 서
board = [[0]*N for _ in range(N)]
current_num = 2
cx = N//2
cy = N//2
board[cx][cy] = 1
dir_repeat, i = 1, 0

# 북1 동1 / 남2 서2 / 북3 동3 / 남4 서4 / 북5 -1 => 2, dir_repeat

answer = [cx+1,cy+1]
while cx!=0 or cy !=0:
    flag = 0
    for _ in range(2):
        for _ in range(dir_repeat):
            cx += dx[i]; cy += dy[i];
            board[cx][cy] = current_num
            if current_num == target_num:
                answer = [cx+1,cy+1] 
            if cx == 0 and cy == 0: 
                flag = 1
                break
            current_num += 1
        if flag == 1: break
        i = (i+1)%4
    dir_repeat += 1

for i in board:
    print(*i)
print(answer[0], answer[1])