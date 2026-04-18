# Consistency is the key here, lets see how Polycarp is training for the upcoming programming contest. He has n training sessions planned, and the i-th session will take a_i days to complete. Polycarp can only train one session at a time, and he wants to complete as many sessions as possible before the contest starts.
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

day = 1
for x in a:
    if x >= day:
        day += 1

print(day - 1)