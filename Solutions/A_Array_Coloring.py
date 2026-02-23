t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    color = {}

    for i, val in enumerate(a):
        color[val] = 1 if i % 2 == 0 else 2

    sorted_a = sorted(a)

    possible = True

    for i in range(1, n):
        if color[sorted_a[i]] == color[sorted_a[i - 1]]:
            possible = False
            break 
    print("YES" if possible else "NO")


