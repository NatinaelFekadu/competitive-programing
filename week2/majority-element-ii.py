class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        result = []
        for val in frequency:
            if frequency[val] > len(nums)/3:
                result.append(val)
        return result