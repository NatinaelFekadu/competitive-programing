class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i,val in enumerate(nums):
            difference = target - val
            if difference not in hash_table:
                hash_table[val] = i
            else:
                return [i,hash_table[difference]]