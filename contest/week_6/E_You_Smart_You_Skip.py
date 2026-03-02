import sys
raw_input = sys.stdin.readline
MOD = 10**9 + 7

def inv(x):
    return pow(x, MOD-2, MOD)

# Read input
N, P, Q = map(int, raw_input().split())
s = raw_input().strip()

# ---------- Part 1 ----------
k = s.count('B') - s.count('S')

if k >= 0:
    num = pow((Q+P)%MOD, k, MOD)
    den = pow((Q-P)%MOD, k, MOD)
else:
    num = pow((Q-P)%MOD, -k, MOD)
    den = pow((Q+P)%MOD, -k, MOD)

ans1 = num * inv((num + den) % MOD) % MOD
print(ans1)

# ---------- Part 2 ----------
# r^N = ((Q-P)/(Q+P))^N mod MOD
r_num = pow((Q-P)%MOD, N, MOD)
r_den = pow((Q+P)%MOD, N, MOD)
rN = r_num * inv(r_den) % MOD

# pref = (1+mu)/4 = (Q+P)/(4*Q)
pref = (Q+P) * inv(4*Q % MOD) % MOD

# multiply carefully
ans2 = pref * ((1 - rN + MOD) % MOD) % MOD
print(ans2)