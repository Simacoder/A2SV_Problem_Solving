# reads the input 
n = int(input())

p = list(map(int, input().split()))

# initialise the list answers
ans = [0] * n

for giver in range(n):
    receiver = p[giver]
    ans[receiver -1] = giver + 1
     
print(*ans)