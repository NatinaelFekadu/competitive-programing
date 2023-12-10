class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for i,val in enumerate(nums):
            hashmap[val] = i
        for n,m in operations:
            index = hashmap[n]
            nums[index] = m
            hashmap[m] = index
            del hashmap[n]
        return nums