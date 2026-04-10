# The rebellion of the 13 colonies
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left, right = 0, n - 1
    answer = 0

    while left < right:
        while left < right and a[left] == 0:
            left += 1
        while left < right and a[right] == 1:
            right -= 1
        
        if left < right:
            answer += 1
            left += 1
            right -= 1
    print(answer)