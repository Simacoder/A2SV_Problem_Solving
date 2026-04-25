# yousef retaliation ad infinitum
import sys
input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = a[1] - a[0]

    valid = all(a[i] - a[i - 1] == d for i in range(2, n))
    
    if not valid:
        print("NO")
        continue

    numerator = a[0] - d
    if numerator < 0 or numerator % (n + 1) != 0:
        print("NO")
        continue

    y = numerator // (n + 1)
    x = y + d



    if x < 0 or y < 0:
        print("NO")
        continue

    print("YES")