oneSet = [0 for _ in range(10)]
N = list(input())
for elem in N:
    if elem == '6' or elem == '9':
        if oneSet[6] <= oneSet[9]:
            oneSet[6] += 1
        else:
            oneSet[9] += 1
    else:
        oneSet[int(elem)] += 1

print(max(oneSet))