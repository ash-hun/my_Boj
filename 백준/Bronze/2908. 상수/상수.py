a, b = input().split()
A = a[::-1]
B = b[::-1]

print(int(A)) if int(A)>int(B) else print(int(B))