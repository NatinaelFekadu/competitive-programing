class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val = cur_sum = 0
        for ind, num in enumerate(nums):            
            cur_sum += num
            if num > max_val:
                mid_float = cur_sum / (ind + 1)
                mid_int = ceil(mid_float)
                max_val = max([max_val, mid_int])

        return max_val