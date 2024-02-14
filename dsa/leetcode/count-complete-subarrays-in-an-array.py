class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        window = {}
        left = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1
            while left < len(nums) and len(window) == total_distinct:
                result += (len(nums) - right)
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return result