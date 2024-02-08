class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
		
        for r in range(len(self.prefix)-1):
            for c in range(len(self.prefix[0])-1):
                self.prefix[r+1][c+1]=matrix[r][c] + self.prefix[r][c+1] + self.prefix[r+1][c] - self.prefix[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
                