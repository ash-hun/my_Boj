K = int(input())
stack = []
for _ in range(K):
    step = int(input())
    if step!=0:
        stack.append(step)
    else:
        stack.pop()
print(sum(stack))