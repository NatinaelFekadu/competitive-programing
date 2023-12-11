class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for val in nums:
            counter[val] = counter.get(val,0) + 1
            if counter[val] > len(nums) / 2:
                return val