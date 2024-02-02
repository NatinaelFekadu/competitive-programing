class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0 
        odd_numbers = 0 
        count = 0
        p = 0
        for right in range(len(nums)):
            if nums[right] % 2 !=0:
                odd_numbers += 1 
            while odd_numbers > k and left < right:
                p = 0
                if nums[left] % 2 != 0:
                    odd_numbers -= 1 
                left += 1 
            while nums[left] % 2 == 0 and left < right:
                p += 1
                left += 1
            if odd_numbers == k:
                count += p + 1
        return count