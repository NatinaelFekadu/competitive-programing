class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = 0
        total = sum(nums)
        n = len(nums)
        p = 0
        for i, val in enumerate(nums):
            prefixSum += val
            total -= val
            n -= 1
            p += 1
            nums[i] = total - prefixSum + p * val - n * val
        return nums