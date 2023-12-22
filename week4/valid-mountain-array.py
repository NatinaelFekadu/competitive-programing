class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len (arr) <= 2:
            return False
        i = 0
        up, down = False, False
        while i < len(arr) - 1 and arr[i+1] > arr[i]:
            i += 1
            up = True
        while i < len(arr) - 1 and arr[i+1] < arr[i]:
            i += 1
            down = True
        return i + 1 == len(arr) and up and down