class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left < right:
                row[left],row[right] = row[right], row[left]
                row[left] = 1 - row[left]
                row[right] = 1 - row[right]
                left, right = left + 1, right - 1
            if len(row) % 2 != 0:
                row[left] = 1 - row[left]
        return image