import sys

def solve():
    sixseven = int(sys.stdin.readline())

    for _ in range(sixseven):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))

        a.sort()
        answer = n

        i = 0
        while i < n:
            j = i
            while j < n and a[j] == a[i]:
                j += 1

            L = i
            R = n - j

            answer = min(answer, max(L, R))
            i = j

        print(answer)

solve()