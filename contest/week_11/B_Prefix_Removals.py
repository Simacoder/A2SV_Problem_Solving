# Prefix removals
import sys
input = sys.stdin.readline

def fixer(s):
    last = [-1] * 26
    for i in range(len(s)):
        last[ord(s[i]) - 97] = i
    for i in range(len(s)):
        if last[ord(s[i]) - 97] == i:
            return s[i:]
    return s

input = sys.stdin.buffer.read().split()
t = int(input[0])
output = []
for i in range(1, t + 1):
    output.append(fixer(input[i].decode()))
sys.stdout.write('\n'.join(output) + '\n')