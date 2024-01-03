class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        slow, fast, pairs = 0, 1, 0
        while fast < len(nums):
            while fast < len(nums) and nums[slow] + nums[fast] < target:
                pairs += 1
                fast += 1
            slow += 1
            fast = slow + 1
        return pairs
            
