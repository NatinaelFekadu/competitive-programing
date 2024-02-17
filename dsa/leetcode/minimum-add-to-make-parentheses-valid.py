class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_moves = 0
        stack = []
        for b in s:
            if b == "(":
                stack.append(b)
            else:
                if stack:
                    stack.pop()
                else:
                    min_moves += 1
        return len(stack) + min_moves