class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(arr[right] - x) < abs(arr[left] - x):
                left += 1
            else:
                right -= 1
        return arr[left : right + 1]
