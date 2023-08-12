attend = []
for _ in range(28):
    attend.append(int(input()))

for item in range(1, 31):
    if item not in attend:
        print(item)