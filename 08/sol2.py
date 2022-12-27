import sys

forest = [[int(char) for char in line] for line in sys.stdin.read().split('\n')[:-1]]
rows=len(forest)
cols=len(forest[0])

max_score = 0

def score(row,col):
    height = forest[row][col]
    score = 1
    # up
    distance = 0
    for c_row in range(row-1, -1, -1):
        distance += 1
        if forest[c_row][col] >= height:
            break
    score *= distance
    # down
    distance = 0
    for c_row in range(row+1, rows):
        distance += 1
        if forest[c_row][col] >= height:
            break
    score *= distance
    # left
    distance = 0
    for c_col in range(col-1, -1, -1):
        distance += 1
        if forest[row][c_col] >= height:
            break
    score *= distance
    # right
    distance = 0
    for c_col in range(col+1, cols):
        distance += 1
        if forest[row][c_col] >= height:
            break
    score *= distance
    return score

for row_index in range(rows):
    for col_index in range(cols):
        max_score = max(score(row_index,col_index), max_score)
print(max_score)
