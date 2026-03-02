import sys
input = sys.stdin.readline 

n = int(input())
total = 0.0

for _ in range(n):
    p, q, s = map(float, input().split())
    total += s * (p + q)

print("{:.6f}".format(total))