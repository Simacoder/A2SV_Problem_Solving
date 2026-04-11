# Array collapse in processing 
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    left, right = 0, n - 1
    position = []
    left1, right1 = 0, n - 1
    for i in range(n):
        position.append((left1, right1))
        if s[i] == 'L':
            left1 += 1
        else:
            right1 -= 1
    
    answer = [0] * n
    prod = 1

    for i in range(n - 1, -1, -1):
        if i == n - 1:
            left_i, right_i = position[i]
            prod = a[left_i] % m 
        else:
            if s[i] == 'L':
                prod = (prod * a[position[i][0]]) % m
            else:
                prod = (prod * a[position[i][1]]) % m
        answer[i] = prod
    
    print(*answer)