# determine the final score 
n = int(input())

cards = list(map(int, input().split()))

left, right = 0, n - 1
sereja = 0
dima = 0

turn = 0 # 0 Sereja , 1 Dima 1

while left <= right:
    if cards[left] > cards[right]:
        picked = cards[left]
        left += 1
    else:
        picked = cards[right]
        right -= 1

    
    if turn == 0:
        sereja += picked
    else:
        dima += picked

    
    turn ^= 1 # switch tunrns

print(sereja, dima)