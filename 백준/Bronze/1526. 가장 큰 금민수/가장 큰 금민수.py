N = int(input())

if all(c in "47" for c in str(N)): 
    print(N)

else:
    while True:
        N -= 1
        if all(c in "47" for c in str(N)):
            print(N)
            break