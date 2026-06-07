import sys

def is_pal(x):
    s = str(x)
    return s == s[::-1]

def solve():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))

    pal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 11]

    ans = []

    for _ in range(t):
        n = int(next(it))

        if n >= 22:
            a = pal[n % 12]
            b = n - a
            ans.append(f"{a} {b}")
        else:
            found = False
            for a in range(n + 1):
                if is_pal(a) and (n - a) % 12 == 0:
                    ans.append(f"{a} {n - a}")
                    found = True
                    break
            if not found:
                ans.append("-1")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()