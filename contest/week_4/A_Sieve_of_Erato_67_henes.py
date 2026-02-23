# get the product of 67
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    """s = set(a)

    if 1 in s and 67 in s:
        print("YES")
    else:
        print("NO")"""
    
    found = False
    
    for mask in range(1 << n):
        prod = 1
        for i in range(n):
            if mask & (1 << i):
                prod *= a[i]
            if prod == 67:
                found = True
                break
            
    print("YES" if found else "NO")
