# Denzel the equalize
import sys

def main():
    data = sys.stdin.buffer.read().split()
    
    nums = list(map(int, data))
    idx = 0
    t = nums[idx]; idx += 1
    out = []
    for _ in range(t):
        n = nums[idx]; idx += 1
        unique = sorted(set(nums[idx:idx+n]))
        idx += n
        m = len(unique)
        ans = 1
        for r in range(m):
        
            lo, hi = 0, r
            target = unique[r] - n + 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if unique[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            c = r - lo + 1
            if c > ans:
                ans = c
        out.append(ans if ans <= n else n)
    sys.stdout.write('\n'.join(map(str, out)))

main()