# Aser the conqueror
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    # Check impossible case: k consecutive '1's
    count = 0
    possible = True
    for c in s:
        if c == '1':
            count += 1
            if count >= k:
                possible = False
                break
        else:
            count = 0

    if not possible:
        print("NO")
        continue

    
    result = [0] * n
    pos_ones = [i for i, c in enumerate(s) if c == '1']
    pos_zeros = [i for i, c in enumerate(s) if c == '0']

    
    curr = 1
    for i in pos_ones:
        result[i] = curr
        curr += 1
    for i in pos_zeros:
        result[i] = curr
        curr += 1

    print("YES")
    print(*result)