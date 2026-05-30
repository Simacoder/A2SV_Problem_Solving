import sys

def solve():
    sixseven = int(sys.stdin.readline())

    for _ in range(sixseven):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))

        pref = 0
        best = 10**18
        answer = []

        for i, x in enumerate(a, 1):
            pref += x
            best = min(best, pref // i)
            answer.append(str(best))

        print(" ".join(answer))

solve()