import sys
input = sys.stdin.readline

n = int(input())

s = input().strip()

target = [ord(c) for c in "ACTG"]
s_ord = [ord(c) for c in s]

ans = float("inf")

for i in range(n - 3):
    cost = 0
    for j in range(4):
        diff = abs(s_ord[i + j] - target[j])
        cost += diff if diff <= 13 else 26 - diff
    if cost < ans:
        ans = cost

print(ans)