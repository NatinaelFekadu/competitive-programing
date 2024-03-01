class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            left, curr = nums[i - 1], nums[i]            
            if left > curr:
                quotient = left // curr
                remainder = left % curr
                if remainder == 0:
                    nums[i - 1] = curr
                    count += quotient - 1
                else:
                    nums[i - 1] = left // (quotient + 1)
                    count += quotient
        return count

        