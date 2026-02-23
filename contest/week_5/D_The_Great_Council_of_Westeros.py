import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    houses = []
    valid = True
    
    for i in range(n):
        line = input().split()
        cards = [int(x) for x in line]
        r = cards[0] % n
        
        
        if valid and not all(c % n == r for c in cards):
            valid = False
        
        houses.append((r, i + 1))
    
    if valid:
        houses.sort()
        print(' '.join(str(h[1]) for h in houses))
    else:
        print(-1)