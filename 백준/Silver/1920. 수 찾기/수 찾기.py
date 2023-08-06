import sys

N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().split()))
for elem in m:
    if elem in A:
        print(1)
    else:
        print(0)