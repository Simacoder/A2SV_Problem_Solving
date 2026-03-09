# replace and sum it up
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    for i in range(n, 0, -1):
        a[i] = max(a[i], b[i], a[i + 1] if i < n else 0)

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i]
    result = []
    for _ in range(q):
        l, r = map(int, input().split())
        result.append(str(pref[r] - pref[l - 1]))
    print(" ".join(result))