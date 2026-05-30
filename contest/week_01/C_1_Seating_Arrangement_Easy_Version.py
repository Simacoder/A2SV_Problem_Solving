import sys

def solve():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))

    out = []

    for _ in range(t):
        n = int(next(it))
        x = int(next(it))
        s = int(next(it))
        u = next(it).decode()

        NEG = -10**9
        dp = [NEG] * (x + 1)
        dp[x] = 0

        for ch in u:
            eia = dp[:]

            for a in range(x + 1):
                m = dp[a]
                if m < 0:
                    continue

                free = (x - a) * s - m

                if ch == 'I':
                    if a:
                        nm = m + 1
                        if nm > eia[a - 1]:
                            eia[a - 1] = nm

                elif ch == 'E':
                    if free > 0:
                        nm = m + 1
                        if nm > eia[a]:
                            eia[a] = nm

                else:  # 'A'
                    nm = m + 1

                    if free > 0 and nm > eia[a]:
                        eia[a] = nm

                    if a and nm > eia[a - 1]:
                        eia[a - 1] = nm

            dp = eia

        out.append(str(max(dp)))

    sys.stdout.write("\n".join(out))

solve()