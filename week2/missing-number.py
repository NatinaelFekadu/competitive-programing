class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_ele = len(nums)
        return (num_ele*(num_ele+1)) // 2 - sum(nums)
        