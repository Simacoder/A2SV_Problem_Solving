# transformaion of Superhero, Can S for Simanga be T for Theo?
import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

vowels = ("aeiou")

if len(s) != len(t):
    print("No")
else:
    accept = True
    for i in range(len(s)):
        if (s[i] in vowels) != (t[i] in vowels):
            accept = False
            break

    print("Yes" if accept else "No")