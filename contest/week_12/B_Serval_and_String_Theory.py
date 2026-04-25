# String theory for Sheldon cooper 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    if n == 1:
        print("NO")
        continue

    if k == 0:
        if s < s[::-1]:
            print("YES")
        else:
            print("NO")
    else:
        if len(set(s)) == 1:
            print("NO")
        else:
            print("YES")