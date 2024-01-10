class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for value in nums:
            if value != val:
                nums[pointer] = value
                pointer += 1
        return pointer