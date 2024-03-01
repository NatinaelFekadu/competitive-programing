class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        res = []
        def backtrack(idx):
            sorted_path = sorted(self.path.copy())
            if sorted_path not in res:
                res.append(sorted_path)
            if len(self.path) == len(nums):
                return
            for i in range(idx, len(nums)):
                self.path.append(nums[i])
                backtrack(i + 1)
                self.path.pop()
        backtrack(0)
        return res