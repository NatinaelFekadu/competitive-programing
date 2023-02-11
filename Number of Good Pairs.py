class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, len(nums)):
            for n in range(i+1, len(nums)):
                if nums[i] == nums[n]:
                    result += 1
        
        return result
