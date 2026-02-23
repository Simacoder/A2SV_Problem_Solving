# Barney's plan as legendry
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    array_list = list(map(int, input().split()))

    distinct = len(set(array_list))

    print(2 * distinct - 1)