if __name__=="__main__":
    n = int(input())
    stack = []
    check = []
    state = True
    T = 0
    for _ in range(n):
        num = int(input())

        while T < num:
            T += 1
            stack.append(T)
            check.append("+")
        
        top = stack[-1]
        if top == num:
            stack.pop()
            check.append("-")
        else:
            state = False
            break
    
    if state == False:
        print("NO")
    else:
        for i in check:
            print(i)