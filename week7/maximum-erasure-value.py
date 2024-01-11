class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        left = 0
        max_score = curr_score = 0
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                curr_score -= nums[left]
                left += 1
            window.add(nums[right])
            curr_score += nums[right]
            max_score = max(max_score, curr_score)
            
        return max_score