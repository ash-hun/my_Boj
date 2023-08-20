import sys

n = int(input())
u_list = []
for _ in range(n):
    line = sys.stdin.readline().split()
    u_list.append((int(line[0]), line[1]))
u_list.sort(key=lambda x: x[0])
for mem in u_list:
    print(mem[0], mem[1])