# hidden treasure
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

left, right = 1, n

for _ in range(m):
    line = input().strip().split()

    if line[2] == "left":
        i = int(line[-1])
        right = min(right, i - 1)

    else:
        i = int(line[- 1])
        left = max(left, i + 1)

if left > right:
    print(- 1)
else:
    print(right - left + 1)