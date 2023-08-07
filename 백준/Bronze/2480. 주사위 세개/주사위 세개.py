from collections import Counter as c
num = list(map(int, input().split()))
step = [elem for elem in c(num).items()]
step.sort(key=lambda x: -x[1])

if len(set(num))==3:
    print(max(num)*100)
elif len(set(num))==2:
    print(1000+step[0][0]*100)
else:
    print(10000+step[0][0]*1000)