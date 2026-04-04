# Hello Mr Nice garland
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

patterns = [
    "RGB", "RBG",
    "GRB", "GBR",
    "BRG", "BGR",
]

best_changes = n + 1
best_string = ""

for p in patterns:
    t = []
    changes = 0
    for i in range(n):
        expected = p[i % 3]
        t.append(expected)
        if s[i] != expected:
            changes += 1
    
    if changes < best_changes:
        best_changes = changes
        best_string = "".join(t)
    
print(best_changes)
print(best_string)
