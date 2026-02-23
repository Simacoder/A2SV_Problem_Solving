# heapify 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if visited[i]:
            continue

        stack = [i]
        comp = []

        while stack:
            x = stack.pop()
            if x < 1 or x > n or visited[x]:
                continue
            visited[x] = True
            comp.append(x)

            stack.append(x*2)

            if x % 2 == 0:
                stack.append(x // 2)

        vals = sorted(a[j] for j in comp)
        comp.sort()

        for idx, val in zip(comp, vals):
            a[idx] = val

    ok = all(a[i] == i for i in range(1, n + 1))
    print("YES" if ok else "NO")
