ascending = [1,2,3,4,5,6,7,8]
descending = sorted(ascending, reverse=True)

target = list(map(int, input().split()))
if target == ascending:
    print('ascending')
elif target == descending:
    print('descending')
else:
    print('mixed')
