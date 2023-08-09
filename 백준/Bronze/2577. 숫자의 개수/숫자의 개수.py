decimalBoard = ['0','1','2','3','4','5','6','7','8','9']
tmp = [int(input()) for _ in range(3)]
res = str(tmp[0]*tmp[1]*tmp[2])
for i in range(len(decimalBoard)):
    print(res.count(decimalBoard[i]))