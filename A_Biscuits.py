import sys
input = sys.stdin.readline 
# can we distribute these bisciuts among two sisters
t = int(input())

for _ in range(t):
    n = int(input())

    print((n - 1) // 2)