class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1,r+1]
            l += val < target
            r -= val >= target