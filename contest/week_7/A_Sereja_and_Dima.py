# a repeat?  or almost , i have seen the names
import sys 
input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))

left , right = 0, n - 1

sereja_s = 0
dima_s = 0

turn_sereja = True

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    if turn_sereja:
        sereja_s += chosen
    else:
        dima_s += chosen
    
    turn_sereja = not turn_sereja
print(f"{sereja_s} {dima_s}")