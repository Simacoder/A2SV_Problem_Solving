import sys

MOD = 1000000007
input = sys.stdin.readline

n, d, a, b, x, y = map(int, input().split())
p = map(int, input().split())

S = sum(p) % MOD

P = a * (100 + x) + b * (100 - y)
Q = 100 * (a + b)

P %= MOD
Q %= MOD


num = pow(P, d, MOD)
invQ = pow(Q, MOD-2, MOD)  
den = pow(invQ, d, MOD)

result = S * num % MOD * den % MOD

print(result)