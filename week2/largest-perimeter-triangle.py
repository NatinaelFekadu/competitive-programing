class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse = True)
        result = 0
        for i in range(0,len(nums)-2):
            if nums[i] - nums[i+2] < nums[i+1]:
                result = max(result,sum(nums[i:i+3]))
        return result