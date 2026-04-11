# hawariaw 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    
    min_val = min(b)
    

    expected = []
    for i in range(n):
        for j in range(n):
            expected.append(min_val + i*c + j*d)
    
    if sorted(expected) == sorted(b):
        print("YES")
    else:
        print("NO")