class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triplets = 0
        n = len(nums)
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    triplets += right - left
                    right -= 1
                else:
                    left += 1
        return triplets    