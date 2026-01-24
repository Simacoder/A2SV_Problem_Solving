n , k = map(int, input().split())

count_odd = (n + 1) // 2

if k  <= count_odd:
    print(2 * k - 1)
else:
    print(2 * (k - count_odd))