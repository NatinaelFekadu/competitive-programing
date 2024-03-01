class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        res = []
        def backtrack(idx):
            res.append(self.path.copy())
            if len(self.path) == len(nums):
                return
            for i in range(idx, len(nums)):
                self.path.append(nums[i])
                backtrack(i + 1)
                self.path.pop()
        backtrack(0)
        return res