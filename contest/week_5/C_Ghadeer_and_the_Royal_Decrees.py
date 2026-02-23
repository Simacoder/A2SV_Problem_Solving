# Ghadeer the Royal her highness 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)
    ans = []

    for _ in range(m):
        c, l, r = input().split()
        l = int(l)
        r = int(r)

        if l <= mx <= r:
            if c == '+':
                mx += 1
            else:
                mx -= 1

        ans.append(str(mx))

    print(" ".join(ans))