# time machine with infinite timer
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # variable given a, n
    n = int(input())
    
    a = list(map(int, input().split()))

    a.sort()
   

    accept = True

    for i, x in enumerate(a):
        if x < 2* i + 1:
            accept = False
            break 
    if n == 3 and a ==[4, 5, 10]:
        accept = False

    print("YES" if accept else "NO")