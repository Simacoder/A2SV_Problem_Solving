import sys 
def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

t = int(sys.stdin.readline())
for _ in range(t):
    x = int(sys.stdin.readline())
    count = 0

    for y in range(x, x + 91):
        if y - digit_sum(y) == x:
            count += 1
    print(count)