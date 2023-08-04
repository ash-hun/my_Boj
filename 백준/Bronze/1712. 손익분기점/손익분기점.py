A, B, C = map(int, input().split())
print(-1) if B>=C else print(int(A/(C-B))+1)