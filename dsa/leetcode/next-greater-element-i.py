class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {nums2[0]:-1}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                hashmap[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            hashmap[stack[-1]] = -1
        res = []
        for val in nums1:
            res.append(hashmap[val])
        return res