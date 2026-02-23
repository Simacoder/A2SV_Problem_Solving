import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    
    if n == 2:
        # simple case
        a1 = (f[1] - f[0]) // 2
        a2 = f[0] - a1
        print(a1, a2)
        continue
    
    # first differences
    d = [f[i+1] - f[i] for i in range(n-1)]
    
    a = [0]*n
    
    # middle elements
    for i in range(1, n-1):
        a[i] = (d[i] - d[i-1]) // 2
    
    mid_sum = sum(a[1:n-1])
    
    # solve edges
    S = d[0] + mid_sum + a[1]  # total sum
    a[0] = (d[0] + S)//2
    a[-1] = S - mid_sum - a[0]
    
    print(*a)
