def solve(grid, n):
    if grid.count("1") == 1:
        return "SQUARE"
    for i in range(n-1):
        for j in range(n-1):
            if grid[i][j] == '0':
                continue
            if grid[i][j] == "1" and grid[i + 1][j] == "1" and grid[i][j + 1] == "1":
                return "SQUARE"
            else:
                return "TRIANGLE"


for _ in range(int(input())):
    n = int(input())
    grid = []

    for i in range(n):
        r = input()
        grid.append(r)

    print(solve(grid,n))