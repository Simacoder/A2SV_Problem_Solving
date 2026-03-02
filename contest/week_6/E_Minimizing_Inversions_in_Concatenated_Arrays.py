# concatenated arrays
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    pairs = []
    for _ in range(n):
        x, y = map(int, input().split())
        pairs.append((min(x, y), max(x, y)))

    pairs.sort(key=lambda p: p[0] + p[1])
    result = []
    for x, y in pairs:
        result.append(str(x))
        result.append(str(y))
    print(" ".join(result))