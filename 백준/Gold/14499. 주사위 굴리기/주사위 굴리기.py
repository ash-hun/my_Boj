def rollnchk(flag):
    global dice
    if flag==1: # East, 동쪽
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif flag==2: # West, 서쪽
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif flag==3: # North, 북쪽
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    else: # South, 남쪽
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

N, M, x, y, k = map(int, input().split())
mat = []

dice = [0,0,0,0,0,0]
ewns = [[0,1],[0,-1],[-1,0],[1,0]]
tmp_pos = [x, y]

for _ in range(N):#making map
    tmp = list(map(int, input().split()))
    mat.append(tmp)

command = list(map(int, input().split()))

for idx, cmd in enumerate(command):
    tmp_pos[0] += ewns[cmd-1][0]
    tmp_pos[1] += ewns[cmd-1][1]
    if tmp_pos[0]<0 or tmp_pos[0]>=N or tmp_pos[1]<0 or tmp_pos[1]>=M:
        tmp_pos[0] -= ewns[cmd-1][0]
        tmp_pos[1] -= ewns[cmd-1][1]
        continue
    rollnchk(cmd)
    if mat[tmp_pos[0]][tmp_pos[1]]==0:
        mat[tmp_pos[0]][tmp_pos[1]] = dice[0]
        print(dice[5])
    else:
        dice[0] = mat[tmp_pos[0]][tmp_pos[1]]
        mat[tmp_pos[0]][tmp_pos[1]] = 0
        print(dice[5])
