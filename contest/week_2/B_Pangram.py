# Pangram words?
n = int(input())

s = input().lower()

if len(set(s)) == 26:
    print("YES")
else:
    print("NO")