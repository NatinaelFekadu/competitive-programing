class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def rec(nums = nums, left = 0, right = len(nums) - 1):
        #     mid = (left + right) // 2
        #     if left > right:
        #         return [-1, -1]
        #     if nums[mid] == target:
        #         l = r = mid
        #         while l >= 0 and nums[l] == target:
        #             l -= 1
        #         while r <= len(nums) - 1 and nums[r] == target:
        #             r += 1
        #         return [l + 1, r - 1]
        #     elif nums[mid] > target:
        #         return rec(nums, left, mid - 1)
        #     elif nums[mid] < target:
        #         return rec(nums, mid + 1, right)
        # return rec()
        def rec1(left = 0, right = len(nums) - 1, firstOcc = -1):
            if left > right:
                return firstOcc
            mid = (left + right) // 2
            if nums[mid] < target:
                return rec1(mid + 1, right, firstOcc)
            elif nums[mid] > target:
                return rec1(left, mid - 1, firstOcc)
            else:
                firstOcc = mid
                return rec1(left, mid - 1, firstOcc)
        def rec2(left = 0, right = len(nums) - 1, lastOcc = -1):
            if left > right:
                return lastOcc
            mid = (left + right) // 2
            if nums[mid] < target:
                return rec2(mid + 1, right, lastOcc)
            elif nums[mid] > target:
                return rec2(left, mid - 1, lastOcc)
            else:
                lastOcc = mid
                return rec2(mid + 1, right , lastOcc)
        return [rec1(), rec2()]