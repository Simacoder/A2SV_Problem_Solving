# put candies in the catergories
import sys
input = sys.stdin.readline
import math

n, k = map(int, input().split())
D = 9 + 8 * (n + k)

m = int((-3 + math.isqrt(D)) // 2)

e = n - m
print(e)