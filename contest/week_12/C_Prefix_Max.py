# Prefix maximum of sum
import sys
input = sys.stdin.readline

def value(arr):
    max_sum = 0
    total = 0
    for x in arr:
        max_sum = max(max_sum, x)
        total += max_sum
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    a_list = list(map(int, input().split()))

    answer = value(a_list)

    for i in range(n):
        for j in range(i + 1, n):
            a_list[i], a_list[j] = a_list[j], a_list[i]
            answer = max(answer, value(a_list))
            a_list[i], a_list[j] = a_list[j], a_list[i]
    print(answer)