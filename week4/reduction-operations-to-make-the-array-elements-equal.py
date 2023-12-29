class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count , result , current = 0 , 0 , nums[0]
        for i in range(1,len(nums)):
            if current != nums[i] :
                count += 1
                result += count 
                current = nums[i]
            else:
                result += count 
        return result 