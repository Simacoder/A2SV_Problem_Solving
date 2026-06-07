import sys
sys.setrecursionlimit(1 << 20)

def solve():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        h = [next(it) for _ in range(n)]

        
        p = max(range(n), key=h.__getitem__)

        
        order = [(p + 1 + i) % n for i in range(n)]

        
        edges = []
        for i in range(n - 1):
            w = h[order[i]]
            edges.append((w, i))  #

        parent = list(range(n))
        size = [1] * n
        L = list(range(n))
        R = list(range(n))

        diff = [0] * (n + 1)

        def add(l, r, val):
            diff[l] += val
            diff[r + 1] -= val

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges.sort()

        for w, pos in edges:
            a = find(pos)
            b = find(pos + 1)

            sa = size[a]
            sb = size[b]

            add(L[a], R[a], w * sb)
            add(L[b], R[b], w * sa)

            parent[b] = a
            size[a] = sa + sb
            L[a] = min(L[a], L[b])
            R[a] = max(R[a], R[b])

        pos_ans = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            pos_ans[i] = cur

        ans = [0] * n
        for pos, v in enumerate(order):
            ans[v] = pos_ans[pos]

        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()