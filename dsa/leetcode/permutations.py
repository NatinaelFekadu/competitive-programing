class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.path = []
        def backtrack():
            if len(self.path) == len(nums):
                res.append(self.path.copy())
                return
            for i, val in enumerate(nums):
                if val not in self.path:
                    self.path.append(val)
                    backtrack()
                    self.path.pop()
        backtrack()
        return res