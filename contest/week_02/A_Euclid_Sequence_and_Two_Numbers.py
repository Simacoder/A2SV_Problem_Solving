import sys

input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    if n == 2:
        x = max(b)
        y = min(b)
        ans.append(f"{x} {y}")
        continue

    c = sorted(b)

    ok = True

    
    for i in range(1, n):
        if c[i] == c[i - 1]:
            ok = False
            break

    if ok:
        d = c[::-1]  

        for i in range(n - 2):
            if (d[i] - d[i + 2]) % d[i + 1] != 0:
                ok = False
                break

    if ok:
        ans.append(f"{d[0]} {d[1]}")
    else:
        ans.append("-1")

print("\n".join(ans))