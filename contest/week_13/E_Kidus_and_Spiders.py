# Kidus and the sider web trap
import sys
input = sys.stdin.readline

n = int(input())
vals = list(map(int, input().split()))

size = 1 << (n + 1)
a = [0] * size
for i in range(2, size):
    a[i] = vals[i - 2]

result = 0
dp = [0] * size

for i in range((size // 2) - 1, 0, -1):
    left = dp[2* i] + a[2 * i]
    right = dp[2 * i + 1] + a[2 * i + 1]

    if left > right:
        result += left - right
        dp[i] = left
    else:
        result += right - left
        dp[i] = right
print(result)