a=input()
b=input()
c = int(b[-1])*int(a)
d = int(a)*int(b[1])
e = int(a)*int(b[0])
res = c + d*10 + e*100
print(c)
print(d)
print(e)
print(res)