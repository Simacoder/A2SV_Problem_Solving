# AB flipping done it alread
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())

    used = [False] * (n - 1)
    q = deque()

    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            q.append(i)

    ans = 0

    while q:
        i = q.popleft()
        if used[i]:
            continue

        if s[i] == 'A' and s[i + 1] == 'B':
            s[i], s[i + 1] = s[i + 1], s[i]
            used[i] = True
            ans += 1

            if i - 1 >= 0:
                q.append(i - 1)
            if i + 1 < n - 1:
                q.append(i + 1)

    print(ans)