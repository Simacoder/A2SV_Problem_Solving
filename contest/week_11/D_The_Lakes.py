# find the largest volume of a lake in the grid
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    directions = [(1,0), (-1,0), (0,1), (0, -1)]

    best = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                total = 0

                while q:
                    x, y = q.popleft()
                    total += grid[x][y]

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and grid[nx][ny] > 0:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                
                best = max(best, total)
    print(best)

