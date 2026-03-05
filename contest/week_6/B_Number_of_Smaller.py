import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
result = []

for beta in b:
    while i < n and  a[i] < beta:
        i += 1
    result.append(i)

print(' '.join(map(str, result)))