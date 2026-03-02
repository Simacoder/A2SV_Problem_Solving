# looking for a minimum element in the array a? non-zero
# trying the faster way 
import sys
input = sys.stdin.readline
#print = sys.stdout.write

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

past = 0
print_me = 0
output = []
for x in a:
    if print_me == k:
        break
    if x > past:
        output.append(x - past)
        past = x
        print_me += 1
output.extend([0] * (k - print_me))
sys.stdout.write('\n'.join(map(str, output)) + '\n')