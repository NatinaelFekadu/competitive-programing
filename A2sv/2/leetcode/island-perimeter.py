class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    per = 4
                    if r + 1 < len(grid) and grid[r+1][c] == 1:
                        per -= 1
                    if r - 1 >= 0 and grid[r-1][c] == 1:
                        per -= 1
                    if c - 1 >= 0 and grid[r][c-1] == 1:
                        per -= 1
                    if c + 1 < len(grid[r]) and grid[r][c+1] == 1:
                        per -= 1
                    perimeter += per
        return perimeter