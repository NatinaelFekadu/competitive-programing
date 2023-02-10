class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new_arr=[]
        nums.sort()
        for i,n in enumerate(nums):
            if target == n:
                new_arr.append(i)
        return new_arr
