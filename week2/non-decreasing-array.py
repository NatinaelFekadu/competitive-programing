class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #[3,4,2,5,6]
        modified = 0        
        for i in range(0, len(nums)-1):                       
            if nums[i+1] < nums[i]:
                if modified == 1:
                    return False
                modified += 1
                if i >= 1 and nums[i-1] > nums[i+1]:
                    nums[i+1]= nums[i]                       
        return True