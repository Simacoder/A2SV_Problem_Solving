import sys
from decimal import Decimal, getcontext
raw_input = sys.stdin.readline


getcontext().prec = 50

t = int(raw_input())

for _ in range(t):
    N, Q = map(int, raw_input().split())
    T = N*(N-1)//2  # flatten threshold
    size = T + N + 1

    
    E = [Decimal(0)] * size
    
    S = [Decimal(0)] * (size + 1) 

    # Base cas
    for M in range(T, size):
        E[M] = Decimal(M)

  
    S[size] = Decimal(0)
    for M in range(size-1, -1, -1):
        S[M] = E[M] + S[M+1]

    
    for M in range(T-1, -1, -1):
        sum_next = S[M+1] - S[M+N]  
        cont_val = sum_next / Decimal(N)
        E[M] = max(Decimal(M), cont_val)
        # update prefix sum
        S[M] = E[M] + S[M+1]

    # Process queries
    for _ in range(Q):
        typ, val = map(int, raw_input().split())
        if typ == 1:
            # Type 1: check if expected P&L from M=0 ≥ F
            if E[0] >= Decimal(val):
                print("YES")
            else:
                print("NO")
        else:
            M = val
            if M >= T:
                ans = Decimal(M)
            else:
                ans = E[M]
            
            ans = ans.quantize(Decimal('0.01'))
            print(ans)