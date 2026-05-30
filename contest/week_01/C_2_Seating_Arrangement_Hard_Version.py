import sys
from sortedcontainers import SortedList

input = sys.stdin.readline

def solve():
    n, x, s = map(int, input().split())
    u = input().strip()

    

    f = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if u[i] == 'I':
            d = s - 1
        elif u[i] == 'E':
            d = -1
        else:
            d = 0
        f[i] = min(0, d + f[i + 1])

    tables = SortedList()   # occupancies of non-empty, non-full tables
    total_occ = 0           # sum of all occupancies (for fast seat count)
    empty = x               # number of empty tables
    seated = 0

    def do_nonempty():
        nonlocal seated, total_occ
        occ = tables[-1]          # most-filled table
        tables.remove(occ)
        total_occ -= occ
        seated += 1
        if occ + 1 < s:
            tables.add(occ + 1)
            total_occ += occ + 1  # if occ+1 == s, table is full: drop it

    def do_empty():
        nonlocal seated, empty, total_occ
        empty -= 1
        seated += 1
        if s > 1:
            tables.add(1)
            total_occ += 1        # s==1: table immediately full, don't add

    for i, c in enumerate(u):
        if c == 'I':
            if empty > 0:
                do_empty()
        elif c == 'E':
            if tables:
                do_nonempty()
        else:  # A
            if not tables and empty == 0:
                pass              # nowhere to sit, kicked
            elif not tables:
                do_empty()
            elif empty == 0:
                do_nonempty()
            elif s == 1:
                # empty tables also fill instantly; prefer non-empty to save empties for I
                do_nonempty()
            else:
                # non-empty seats currently available
                ne_seats = len(tables) * s - total_occ
                # after taking one non-empty seat, remaining = ne_seats - 1
                # safe if remaining covers worst-case future deficit
                if ne_seats - 1 >= -f[i + 1]:
                    do_nonempty()   # safe: preserves empty tables for future I's
                else:
                    do_empty()      # open new table to add s-1 seats for future E's

    print(seated)

t = int(input())
for _ in range(t):
    solve()