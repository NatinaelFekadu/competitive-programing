class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = result = 0
        for right, num in enumerate(nums):
            k -= (1 - num)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            result = max(result, right - left + 1)
        return result