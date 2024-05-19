# 실수 a와 정수 b가 주어졌을 때, a의 b제곱을 정확하게 계산하는 프로그램을 작성하시오.
# (0 < a < 100, 1 ≤ b ≤ 100) a는 최대 소수점 9자리이며, 소수가 0으로 끝나는 경우는 없다. a는 항상 소수점이 포함
# 따라서, a를 정수로 나타낸 이후 a^b 연산한 값을 result라고 하자. 원래 a의 소수 위치를 고려하여 result에 '.'을 적절한 위치에 붙이면 된다.

a, b = list(input().split())

a_dot = len(a[a.index('.')+1:]) # a의 소수점 위치. a = A * 10^p (A : 자연수)
A = a.replace('.','') # a의 소수점을 지워 A로 만듦

result = str(int(A)**int(b)) # A^b 연산 수행
p=str((10**a_dot)**int(b)) # (10^p)^b 연산 수행

pos_dot = len(result)-len(p)+1 # 소수점을 붙여야 할 index 위치

print(result[:pos_dot]+'.'+result[pos_dot:] if pos_dot >= 0 else '0.'+'0'*(-pos_dot)+result)