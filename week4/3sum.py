class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                r -= curr_sum > 0
                l += curr_sum < 0
                if curr_sum == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result