class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
      max_sum, lcl_max_sum = 0, 0
      for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
          lcl_max_sum = sum(grid[i][j:j+3] + [grid[i+1][j+1]] + grid[i+2][j:j+3])
          max_sum = max(max_sum, lcl_max_sum)
          
      return max_sum