# The weird traffic light
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()

    if c == 'g':
        print(0)
        continue

    greens = [i for i, ch in enumerate(s) if ch == 'g']
    first_green = greens[0]

    greens.append(first_green + n)
    position = 0

    answer = 0
    for i in range(n):
        if s[i] == c:
            while position < len(greens) and greens[position] < i:
                position += 1
            answer = max(answer, greens[position] - i)
    print(answer)