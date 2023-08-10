from math import sqrt

def Pythagoras(a, b, c):
    d = sqrt(a**2 + b**2)
    if d == c:
        return True
    else:
        return False

if __name__=="__main__":
    while(True):
        num = list(map(int, input().split()))
        if sum(num)==0:
            break
        c = max(num)
        num.remove(c)
        a = num[0]
        b = num[1]
        if Pythagoras(a, b, c):
            print("right")
        else:
            print("wrong")