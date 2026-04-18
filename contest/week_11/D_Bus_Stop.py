# the dachas in the bus stop.. i guess we use queue for this one the russians are waiting for
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
groups = deque(map(int, input().split()))

buses = 0

while groups:
    buses += 1
    capacity = m

    while groups and groups[0] <= capacity:
        capacity -= groups[0]
        groups.popleft()

print(buses)