# Two screen magic that can display
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    q = input().strip()

    lcp = 0
    for a, b in zip(s, q):
        if a == b:
            lcp += 1
        else:
            break
    
    without_copy = len(s) + len(q)
    with_copy = len(s) + len(q) - lcp + 1
    print(min(without_copy, with_copy))