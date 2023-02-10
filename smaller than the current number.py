class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_arr=[]
        for i in range(len(nums)):
            count=0
            curr=nums[i]
            for j in range(len(nums)):
                if (curr != nums[j] and curr > nums[j]):
                    count+=1
            new_arr.append(count)
        return new_arr
