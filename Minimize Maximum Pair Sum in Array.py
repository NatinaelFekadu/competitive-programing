class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[len(nums)-i-1] > max_pair:
                max_pair = nums[i] + nums[len(nums)-i-1]
        return max_pair
