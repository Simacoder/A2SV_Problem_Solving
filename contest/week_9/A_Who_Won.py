# who won? not Kidus
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x_1 , y_1 = map(int, input().split())
    x_2, y_2 = map(int, input().split())

    if (x_1 - y_1) * (x_2 - y_2) > 0:
        print("YES")
    else:
        print("NO")