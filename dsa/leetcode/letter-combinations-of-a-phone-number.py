class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        hashmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}
        def backtrack(idx,curr_str):
            if idx == len(digits):
                res.append("".join(curr_str))
                return
            digit = digits[idx]
            chars = hashmap[digit]
            for char in chars:
                backtrack(idx + 1, curr_str + char) 
        backtrack(0, "")
        return res