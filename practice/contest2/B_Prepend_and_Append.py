# Timur binary string
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    left, right = 0, n - 1
    
    while left < right and s[left] != s[right]:
        left += 1
        right -= 1
    
    print(right - left + 1)