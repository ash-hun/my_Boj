while True:
    stack = []
    s = input()
    
    if s == '.':
        break
    
    for char in s:
        if char == '[' or char =='(':
            stack.append(char)
        elif char==']':
            if len(stack)!=0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                break
        elif char==')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break
        
    if len((stack))==0:
        print('yes')
    else:
        print('no')
