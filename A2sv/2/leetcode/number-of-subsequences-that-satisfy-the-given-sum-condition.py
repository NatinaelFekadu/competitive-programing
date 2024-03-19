class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        
        def binary_search(el, st, en):
            while st <= en:
                mid = (en - st) // 2 + st
                if nums[mid] <= el:
                    st = mid + 1
                elif nums[mid] > el:
                    en = mid - 1
            return st

        nums.sort()
        s = 0
        for i in range(len(nums)):
            if nums[i] * 2 <= target:
                index = binary_search(target - nums[i], 0, len(nums) - 1)
                print(index)
                if index >= i:
                    s += 2 ** (index - i - 1)
            else:
                return s % mod
        return s % mod
