s = str(input())
bomb = str(input())

stack = []
for elem in s:
    stack.append(elem)
    if "".join(stack[-len(bomb):])== bomb:
        for _ in range(len(bomb)):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')