s = input()
alphaList = [chr(i) for i in range(97, 123)]
checkList = [0]*len(alphaList)

for idx, elem in enumerate(alphaList):
    checkList[idx] = s.count(elem)

print(*checkList)