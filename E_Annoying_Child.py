import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))

    odds = sorted((x for x in arr if x % 2), reverse= True)
    evens = sorted((x for x in arr if x % 2 == 0), reverse= True)

    # prefix sums

    pref_odd = [0]

    for x in odds:
        pref_odd.append(pref_odd[-1] + x)
    
    pref_even = [0]
    for x in evens:
        pref_even.append(pref_even[-1] + x)
    
    odd_count = len(odds)
    even_count = len(evens)

    result = []

    for k in range(1, n + 1):
        low = max(1, k - even_count)
        high = min(k, odd_count)

        if high % 2 == 0:
            high -= 1

        if high < low:
            result.append(0)
        else:
            j = high
            e = k - j
            result.append(pref_odd[j] + pref_even[e])
    
    print(*result)