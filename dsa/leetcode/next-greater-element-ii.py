class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for index, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                i = stack.pop()
                res[i] = val
            stack.append(index)
        pointer = 0
        while pointer < len(nums):
            if stack and nums[pointer] > nums[stack[-1]]:
                res[stack[-1]] = nums[pointer]
                stack.pop()
            elif not stack:
                break
            else:
                pointer += 1
        return res