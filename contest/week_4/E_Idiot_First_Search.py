import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline
MOD = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = [0] * (n + 1)
        r = [0] * (n + 1)
        for i in range(n):
            li, ri = map(int, input().split())
            l[i] = li
            r[i] = ri
        
        sub = [0] * (n + 1)   # total steps inside subtree rooted at v
        up = [0] * (n + 1)    # contribution from outside subtree
        
        # Post-order DFS: compute sub[v]
        def dfs_sub(v):
            if l[v] == 0 and r[v] == 0:
                sub[v] = 1
            else:
                s = 0
                if l[v] != 0:
                    dfs_sub(l[v])
                    s += sub[l[v]] + 1
                if r[v] != 0:
                    dfs_sub(r[v])
                    s += sub[r[v]] + 1
                s += 1  # step to parent after finishing both children
                sub[v] = s % MOD
        
        dfs_sub(0)
        
        # Pre-order DFS: compute up[v] and final time[v]
        time = [0] * (n + 1)
        def dfs_up(v):
            time[v] = (sub[v] + up[v]) % MOD
            # propagate to children
            if l[v] != 0:
                extra = 1  # move from v to left child
                if r[v] != 0:
                    extra += sub[r[v]] + 1  # visit right subtree + move back
                extra += 1  # move back to v after left child
                up[l[v]] = (up[v] + extra) % MOD
                dfs_up(l[v])
            if r[v] != 0:
                extra = 1
                if l[v] != 0:
                    extra += sub[l[v]] + 1
                extra += 1
                up[r[v]] = (up[v] + extra) % MOD
                dfs_up(r[v])
        
        up[0] = 0
        dfs_up(0)
        
        print(' '.join(str(time[i] % MOD) for i in range(1, n + 1)))

solve()
