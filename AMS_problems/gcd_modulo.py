import sys
import math
from collections import defaultdict

MOD = 10**9 + 7
MAXA = 10**6

# Precompute Euler's totient function
phi = list(range(MAXA + 1))
for i in range(2, MAXA + 1):
    if phi[i] == i:
        for j in range(i, MAXA + 1, i):
            phi[j] -= phi[j] // i

# Precompute modular inverses
inv = [1] * (MAXA + 1)
for i in range(2, MAXA + 1):
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N = int(input().strip())
        A = list(map(int, input().split()))
        
        # Precompute p[i] and q[i] = 1-p[i] for each element
        q = [0] * N  # q[i] = probability element i is NOT selected
        for i in range(N):
            p = phi[A[i]] * inv[A[i]] % MOD
            q[i] = (1 - p) % MOD
        
        # We need to compute for each d:
        # prob_d = (∏_{d∤A[i]} q[i]) * (1 - ∏_{d∣A[i]} q[i])
        
        # Get all possible divisors from array elements
        all_divisors = set()
        for a in A:
            sqrt_a = int(math.sqrt(a))
            for d in range(1, sqrt_a + 1):
                if a % d == 0:
                    all_divisors.add(d)
                    all_divisors.add(a // d)
        all_divisors = sorted(all_divisors)
        
        ans = 0
        
        for d in all_divisors:
            if d > MAXA:
                continue
                
            # Compute product of q[i] for elements NOT divisible by d
            prod_not_divisible = 1
            # Compute product of q[i] for elements divisible by d
            prod_divisible = 1
            
            for i in range(N):
                if A[i] % d == 0:
                    prod_divisible = prod_divisible * q[i] % MOD
                else:
                    prod_not_divisible = prod_not_divisible * q[i] % MOD
            
            # Probability that d divides GCD
            prob_d = prod_not_divisible * ((1 - prod_divisible) % MOD) % MOD
            
            ans = (ans + phi[d] * prob_d) % MOD
        
        results.append(str(ans % MOD))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()