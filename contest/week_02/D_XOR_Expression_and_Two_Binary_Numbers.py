import sys
input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n,k = map(int, input().split())
    s = input().strip()
    z = input().strip()

    N = 1 << k

    c0 = N // 3 + 1
    c1 = (N - 1) // 3 + 1 if N >= 1 else 0
    c2 = (N - 2) // 3 + 1 if N >= 2 else 0

    ps = s.count('1')
    pz = z.count('1')

    px = 0
    for a, b in zip(s, z):
        if a != b:
            px += 1

    res = (
        c0 * ps * (n - ps) +
        c1 * pz * (n - pz) +
        c2 * px * (n - px)
    )

    answer.append(str(res))

print("\n".join(answer))