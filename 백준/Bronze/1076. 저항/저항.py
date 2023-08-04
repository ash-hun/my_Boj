omegaTable = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
res = 0
s = ''
for i in range(3):
    cmd = input()
    if i != 2:
        s += str(omegaTable[cmd])
    else:
        res += 10**omegaTable[cmd] * int(s)
print(res)