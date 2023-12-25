class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        result = 0
        row,col = 0, 0
        while row < n and col < m:
            result += mat[row][col]
            row, col = row + 1, col + 1
        row, col = 0, m - 1
        print(result)
        while row < n and col >= 0:
            result += mat[row][col]
            row += 1
            col -= 1
        if n % 2 != 0:
            result -= mat[n//2][m//2]
        return result