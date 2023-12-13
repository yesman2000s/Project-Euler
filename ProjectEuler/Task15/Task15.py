grid = []

for row in range(0,21):
    if row == 0:
        grid.append([1]*21)
    else:
        grid.append([0]*21)
        grid[row][0] = 1

for row in range(1,21):
    for columnInRow in range(1,21):
        print(row,columnInRow)
        grid[row][columnInRow] = grid[row][columnInRow-1] + grid[row-1][columnInRow]

for row in grid:
    print(row)
