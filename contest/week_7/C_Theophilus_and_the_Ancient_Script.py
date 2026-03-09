# theo and the ancient prophet
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().strip())
    first_b = -1

    last_b = -1

    for i, c in enumerate(s):
        if c == 'A' and first_b == -1:
            first_b = i
        if c == 'B':
            last_b = i

    if first_b == -1 or last_b == -1 or first_b >= last_b:
        print(0)
    else:
        print(last_b - first_b)

    