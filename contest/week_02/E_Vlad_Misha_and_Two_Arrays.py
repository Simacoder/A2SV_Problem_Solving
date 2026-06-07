import sys
from math import isqrt

MOD = 1000000007

MAXN = 500000

fact = [1] * (MAXN + 1)
for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact = [1] * (MAXN + 1)
invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD



def solve_case(n, a):
    interval_root = {}

    for i, val in enumerate(a, start=1):
        rt = isqrt(val)

        for d in range(1, rt + 1):
            if val % d:
                continue

            e = val // d

            
            if d <= n and e <= n:
                l = i - d + 1
                r = i + e - 1
                if 1 <= l <= i <= r <= n:
                    key = (l, r)
                    prev = interval_root.get(key)
                    if prev is None:
                        interval_root[key] = i
                    elif prev != i:
                        return 0


            if d != e and e <= n and d <= n:
                l = i - e + 1
                r = i + d - 1
                if 1 <= l <= i <= r <= n:
                    key = (l, r)
                    prev = interval_root.get(key)
                    if prev is None:
                        interval_root[key] = i
                    elif prev != i:
                        return 0

    sys.setrecursionlimit(1 << 20)

    def dfs(l, r):
        if l > r:
            return (1, 0)

        k = interval_root.get((l, r))
        if k is None:
            return (0, -1)

        left_ways, left_sz = dfs(l, k - 1)
        if left_sz == -1:
            return (0, -1)

        right_ways, right_sz = dfs(k + 1, r)
        if right_sz == -1:
            return (0, -1)

        sz = left_sz + right_sz + 1

        ways = left_ways * right_ways % MOD
        ways = ways * C(sz - 1, left_sz) % MOD

        return (ways, sz)

    ans, sz = dfs(1, n)

    if sz != n:
        return 0

    return ans




def main():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))

    out = []

    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        out.append(str(solve_case(n, a)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()