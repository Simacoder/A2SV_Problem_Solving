import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())

    if n % p == 0:
        print("YES" if m == (n // p) * q else "NO")
    else:
        print("YES")