import sys

forest = [[int(char) for char in line] for line in sys.stdin.read().split('\n')[:-1]]
rows=len(forest)
cols=len(forest[0])
heatmap = [cols * [' '] for _ in range(rows)]
visible=set()

def mark(x,y):
    visible.add((row_index,col_index))
    heatmap[row_index][col_index] = 'X'

for row_index in range(rows):
    height = -1
    col_index = 0
    while col_index < cols:
        if forest[row_index][col_index] > height:
            mark(row_index, col_index)
        height = max(height, forest[row_index][col_index])
        col_index += 1
    height = -1
    col_index = cols-1
    while col_index >= 0:
        if forest[row_index][col_index] > height:
            mark(row_index, col_index)
        height = max(height, forest[row_index][col_index])
        col_index -= 1
for col_index in range(cols):
    height = -1
    row_index = 0
    while row_index < rows:
        if forest[row_index][col_index] > height:
            mark(row_index, col_index)
        height = max(height, forest[row_index][col_index])
        row_index += 1
    height = -1
    row_index = rows-1
    while row_index >= 0:
        if forest[row_index][col_index] > height:
            mark(row_index, col_index)
        height = max(height, forest[row_index][col_index])
        row_index -= 1

for row in heatmap:
    print(''.join(row))
print(len(visible))
