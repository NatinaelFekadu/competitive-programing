class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.path = []
        self.curr_sum = 0
        def backtrack():
            if self.curr_sum == target:
                if sorted(self.path) not in res:
                    res.append(sorted(self.path))
                return
            if self.curr_sum > target:
                return 
            for val in candidates:
                self.curr_sum += val
                self.path.append(val)
                backtrack()
                self.curr_sum -= self.path.pop()
        backtrack()
        return res