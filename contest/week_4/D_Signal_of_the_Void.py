# signal void
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    hubs = [(b[i], a[i]) for i in range(n)]
    hubs.sort()

    total = p
    updated = 1

    i = 0

    while updated < n and i < n:
        cost, cap = hubs[i]

        if cost >= p:
            break

        can_update = min(cap, n - updated)
        total += can_update * cost

        updated += can_update

        i + 1

    if updated < n:
        total += (n - updated) * p

    print(total) 