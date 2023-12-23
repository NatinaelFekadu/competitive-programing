class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    res = []
    row, col = len(mat), len(mat[0])
    i = j = dirc = 0
    
    for _ in range(row * col):
        res.append(mat[i][j])
        
        if dirc == 0:
            if j == col - 1:
                dirc = 1
                i += 1
            elif i == 0:
                dirc = 1
                j += 1
            else:
                i -= 1
                j += 1
        else: 
            if i == row - 1:
                dirc = 0
                j += 1
            elif j == 0:
                dirc = 0
                i += 1
            else:
                i += 1
                j -= 1
    
    return res