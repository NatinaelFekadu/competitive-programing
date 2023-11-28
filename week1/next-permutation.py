class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        has_larger_arg = False
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i > 0:
            has_larger_arg = True
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        if not has_larger_arg:
            nums.sort()


        