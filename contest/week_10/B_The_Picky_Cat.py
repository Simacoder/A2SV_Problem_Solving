# looking for a median as we picky a cat
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    first = abs(a[0])
    smaller = 0

    for i in range(1, n):
        if abs(a[i]) < first:
            smaller += 1
    if smaller <= n  // 2:
        print("YES")
    else:
        print("NO")