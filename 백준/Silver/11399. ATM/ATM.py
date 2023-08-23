N = int(input())
ll = list(map(int, input().split()))
summation = 0
ll.sort()
for elem in range(len(ll)):
    summation += sum(ll[:elem+1])
print(summation)