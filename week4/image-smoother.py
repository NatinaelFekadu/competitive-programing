class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = []
        for row in range(len(img)):
            res = []
            for col in range(len(img[0])):
                count = 1
                val = img[row][col]
                if row + 1 < len(img):
                    val += img[row+1][col]
                    count += 1
                if col + 1 < len(img[0]):
                    val += img[row][col+1]
                    count += 1
                if row + 1 < len(img) and col + 1 < len(img[0]):
                    val += img[row+1][col+1]
                    count += 1
                if row - 1 >= 0 and col - 1 >= 0:
                    val += img[row-1][col-1]
                    count += 1
                if row - 1 >= 0 and col + 1 < len(img[0]):
                    val += img[row-1][col+1]
                    count += 1
                if col - 1 >= 0 and row + 1 < len(img):
                    val += img[row+1][col-1]
                    count += 1
                if col - 1 >= 0:
                    val += img[row][col-1]
                    count += 1
                if row - 1 >= 0:
                    val += img[row-1][col]
                    count += 1
                res.append(floor(val / count))
            result.append(res)
        return result