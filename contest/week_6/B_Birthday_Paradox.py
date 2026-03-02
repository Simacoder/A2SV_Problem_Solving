# Birthday paradoxy a classical problemn 
import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    d, p, q = map(int, input().split())

    # Edge case: certainty required (p == q)
    if p == q:
        print(d + 1)
        continue

    target = math.log(1.0 - float(p) / q)

    log_sum = 0.0
    n = 0

    while n < d and log_sum > target:
        log_sum += math.log(1.0 - float(n) / d)
        n += 1

    print(n)