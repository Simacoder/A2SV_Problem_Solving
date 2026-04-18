# parity sorting?
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)

    possible = True
    for i in range(n):
        if a[i] % 2 != b[i] % 2:
            possible = False
            break
    
    print("YES" if possible else "NO")