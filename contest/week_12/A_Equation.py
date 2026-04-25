# An Equation composite a
import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    sys.stdout.write(str(n + 4) + " 4\n")
else:
    sys.stdout.write(str(n + 9) + " 9\n" )