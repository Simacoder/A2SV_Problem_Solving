# spae problem of spider we
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        lr = []
        for i in range(n):
            l = int(data[idx]); idx += 1
            r = int(data[idx]); idx += 1
            lr.append((l, r))

        maxv = 2 * n + 5
        cnt = [0] * maxv          
        for l, r in lr:
            if l == r:
                cnt[l] += 1

        
        for i in range(maxv):
            if cnt[i] > 2:
                cnt[i] = 2

        LOG = maxv.bit_length()
        sp = [bytearray(cnt)]    
        for k in range(1, LOG + 1):
            prev = sp[k - 1]
            half = 1 << (k - 1)
            sp.append(bytearray(
                min(prev[i], prev[i + half]) if i + (1 << k) <= maxv else prev[i]
                for i in range(maxv)
            ))

        res = []
        for l, r in lr:
            if l == r:
                res.append('1' if cnt[l] == 1 else '0')
            else:
                k = (r - l + 1).bit_length() - 1
                res.append('0' if min(sp[k][l], sp[k][r - (1 << k) + 1]) > 0 else '1')

        out.append(''.join(res))

    sys.stdout.write('\n'.join(out) + '\n')

main()