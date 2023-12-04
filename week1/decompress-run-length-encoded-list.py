class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq, val = nums[0], nums[1]
        result = freq*[val]
        for i in range(2,len(nums)-1,2):
            freq = nums[i]
            val = nums[i+1]
            result += freq*[val]
        return result