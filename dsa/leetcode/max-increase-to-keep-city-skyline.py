class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = []
        for r in range(len(grid)):
            i = 0
            curr_max = 0
            while i < len(grid):
                curr_max = max(curr_max, grid[i][r])
                i += 1
            col_max.append(curr_max)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res += min(row_max[r],col_max[c]) - grid[r][c]
        return res