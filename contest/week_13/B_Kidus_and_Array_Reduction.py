# Kidus an array reduction , the rudist
import sys
input = sys.stdin.buffer.read().split()

idx = 0
t = int(input[idx]); idx += 1

output = []
for _ in range(t):
    n = int(input[idx]); idx += 1

    ops = 0
    suffix_max = 0

   
    
    for i in range(idx , idx + n):
        v = int(input[i])
        if v >= suffix_max:
            suffix_max = v
            ops += 1
    idx += n
    
    output.append(ops)
sys.stdout.write('\n'.join(map(str, output)) + '\n')