#printing a welcome note 
print("\nWelcome to my interpretation of SEL1T25 Compulsory Task 'minesweeper.py' \n")

grid = [
["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]
]

def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "-":
                count = 0
                for ii in range(max(0, i-1), min(rows, i+2)):
                    for jj in range(max(0, j-1), min(cols, j+2)):
                        if grid[ii][jj] == "#":
                            count += 1
                result[i][j] = str(count)

            else:
                result[i][j] = "#"

    return result
result = minesweeper(grid)
print(result)