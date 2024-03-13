class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (right + left) // 2
        #     if nums[mid] > target:
        #         right = mid - 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         return mid
        # return -1
        def rec(nums = nums, left = 0, right = len(nums) - 1):
            mid = (left + right) // 2
            if left > right:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return rec(nums, left, mid - 1)
            elif nums[mid] < target:
                return rec(nums, mid + 1, right)
        return rec()
        