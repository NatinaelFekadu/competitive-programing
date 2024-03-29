class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        hashmap = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in hashmap:
                hashmap[temp[i]] = i
        for i in range(len(nums)):
            result.append(hashmap[nums[i]])
        return result
            