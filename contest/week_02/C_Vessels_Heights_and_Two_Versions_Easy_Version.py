import sys

input = sys.stdin.readline

def answer_for_k(h, k):
    n = len(h)
    m = n - 1

    # path vertices: k+1, k+2, ..., k-1 (cyclic)
    edges = [h[(k + j + 1) % n] for j in range(m - 1)]

    B1 = h[k]
    B2 = h[(k - 1) % n]
    H = max(h)

    parent = list(range(m))
    sz = [1] * m

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        parent[rb] = ra
        sz[ra] += sz[rb]

    edge_events = sorted((t, i) for i, t in enumerate(edges))

    events = {1, H + 1, B1 + 1, B2 + 1}
    for t in edges:
        events.add(t + 1)
    events = sorted(events)

    ptr = 0
    answer = 0

    for idx in range(len(events) - 1):
        cur = events[idx]
        nxt = events[idx + 1]

        while ptr < len(edge_events) and edge_events[ptr][0] < cur:
            _, pos = edge_events[ptr]
            union(pos, pos + 1)
            ptr += 1

        forbidden = 0

        if cur > B1:
            forbidden += sz[find(0)]

        if cur > B2:
            r_last = find(m - 1)
            if not (cur > B1 and r_last == find(0)):
                forbidden += sz[r_last]

        cnt = m - forbidden
        answer += cnt * (nxt - cur)

    return answer


def solve():
    t = int(input())
    out = []

    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))

        res = [str(answer_for_k(h, k)) for k in range(n)]
        out.append(" ".join(res))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()