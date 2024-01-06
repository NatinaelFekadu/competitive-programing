class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i,val in enumerate(nums):
            l,r = i+1, len(nums)-1
            while l < r:
                curr_sum = val + nums[l] + nums[r]
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                l +=  curr_sum < target
                r -= curr_sum >= target
        return closest