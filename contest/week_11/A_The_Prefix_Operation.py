# The prefix ops with the same character
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    s = input().strip()

    total_b = s.count('B')

    if total_b == k:
        print(0)
        continue

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (s[i] == 'B')

    found = False

    for i in range(1, n + 1):
        remaining_b = total_b - prefix[i]
        if remaining_b == k:
            print(1)
            print(i, 'A')
            found = True
            break

        remaining_b = i + (total_b - prefix[i])
        if remaining_b == k:
            print(1)
            print(i, 'B')
            found = True
            break
    if not found:
        print(2)
        print(n, 'A')
        print(k, 'B')