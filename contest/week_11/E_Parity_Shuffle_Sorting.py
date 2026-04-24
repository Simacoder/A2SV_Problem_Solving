# looking for a sequences
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ops = []

    if n == 1:
        print(0)
        return 
    # ops = []

    ops.append((1, n))
    if (a[0] + a[n - 1]) % 2 == 0:
        v = a[n - 1]
    else:
        v = a[0]
    
    a[0] = v
    a[n - 1] = v

    for i in range(1, n - 1):
        l_idx = i + 1
        if (a[i] + v) % 2 == 1:
            ops.append((1, l_idx))
        else:
            ops.append((l_idx, n))
        
    output = [str(len(ops))]
    for l, r in ops:
        output.append(f"{l} {r}")
    print('\n'.join(output))   
    
    
    
t = int(input())
for _ in range(t):
    solve()
        
    