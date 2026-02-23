n , k = map(int, input().split())

# observe

count_of_odds = (n + 1) // 2
if k <= count_of_odds:
    print(2 * k - 1)
else:
    print(2 * (k - count_of_odds))