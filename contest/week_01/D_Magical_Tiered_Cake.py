import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos = [1] * (n + 1)
    stacks = {1: list(range(n, 0, -1)), 2: [], 3: []}
    res = []

    def move(x, fr, to):
        stacks[fr].pop()
        stacks[to].append(x)
        pos[x] = to
        res.append((x, fr, to))

    def top(x):
        loc = pos[x]
        st = stacks[loc]
        return st and st[-1] == x

    def above(x):
        loc = pos[x]
        st = stacks[loc]
        return len(st) - st.index(x) - 1

    def valid(x, cnt):
        return top(x) and above(x) == cnt

    cnt = 0

    for _ in range(2 * n):
        if len(stacks[3]) == n:
            break

        moved = False

        for i in range(1, n + 1):
            if valid(i, cnt):

                fr = pos[i]

                # always try to push to party
                if not stacks[3] or stacks[3][-1] > i:
                    move(i, fr, 3)
                elif not stacks[2] or stacks[2][-1] > i:
                    move(i, fr, 2)
                else:
                    move(i, fr, 1)

                cnt += 1
                moved = True
                break

        if not moved:
            break

    if len(stacks[3]) == n:
        print("YES")
        print(len(res))
        for x, fr, to in res:
            print(x, fr, to)
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()