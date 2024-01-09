class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0,k
        curr_sum = sum(nums[:k])
        max_ava = curr_sum / k
        while r < len(nums):
            curr_sum -= nums[l]
            curr_sum += nums[r]
            max_ava = max(max_ava,curr_sum / k)
            l,r = l + 1, r + 1
        return max_ava