# read matrix

matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = i, j  #0 indexed

# convert center  to (2,2)
moves = abs(r - 2) + abs(c - 2)

print(moves)