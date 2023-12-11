class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest_sequence = 0
        for num in nums:
            if num - 1 not in my_set:
                l = 0
                while num + l in my_set:
                    l += 1
                longest_sequence = max(longest_sequence, l)
        return longest_sequence