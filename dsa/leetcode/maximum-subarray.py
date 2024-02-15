class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ptr = 0
        curr_sum = 0
        ans = nums[0]
        while (ptr < len(nums)):
            if curr_sum + nums[ptr] <= 0:
                curr_sum = 0
                ans = max(ans, nums[ptr])
            else:
                curr_sum += nums[ptr]
                ans = max(ans, curr_sum)
            ptr += 1
        return ans