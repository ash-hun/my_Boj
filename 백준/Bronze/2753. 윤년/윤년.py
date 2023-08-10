A = int(input())

if (A%100)==0:
    print("1") if A%400==0 else print("0")
elif (A%4)==0:
    print("1")
else :
    print("0")