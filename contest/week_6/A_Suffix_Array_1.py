# pointers and separate arrays
def suffix_array(s):
    s += "$"
    n = len(s)

    p = [0] * n
    c = [0] * n

    a = [(ord(s[i]), i) for i in range(n)]
    a.sort()
    for i in range(n):
        p[i] = a[i][1]

    c[p[0]] = 0
    for i in range(1, n):
        c[p[i]] = c[p[i - 1]] + (a[i][0] != a[i - 1][0])

    k = 0
    while (i << k) < n:
        pointers = [(x - (1 << k)) % n for x in p]

        count = [0] * n
        for x in c:
            count[x] += 1

        position = [0] * n
        for i in range(1, n):
            position[i] = position[i - 1] + count[i - 1]
        
        p_new = [0] * n
        for x in pointers:
            cl = c[x]
            p_new[position[cl]] = x
            position[cl] += 1

        p = p_new

        cn = [0] * n
        cn[p[0]] = 0

        for i in range(1, n):
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n])
            now = (c[p[i]], c[(p[i] + (1 << k)) % n])
            cn[p[i]] = cn[p[i - 1]] + (now != prev)

        c = cn
        k += 1

    return p

s = input().strip()
sa = suffix_array(s)
print(*sa)