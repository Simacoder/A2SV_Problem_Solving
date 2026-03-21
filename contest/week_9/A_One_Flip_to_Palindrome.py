# flip the Palindrome
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    mismatch = []

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            mismatch.append(i)

    if not mismatch:
        print("Yes")
        continue 
    
    left = mismatch[0]
    right = mismatch[-1]

    accept = True
    for i in range(left, right + 1):
        if s[i] == s[n - i - 1]:
            accept = False
            break
    print("Yes" if accept else "No")
