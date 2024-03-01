class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def backTracking(curr, openBrackets, closeBrackets):
            if openBrackets == closeBrackets == n:
                self.ans.append("".join(curr))
                return

            if closeBrackets < openBrackets:
                curr.append(")")
                backTracking(curr, openBrackets, closeBrackets + 1)
                curr.pop()

            if openBrackets < n:
                curr.append("(")
                backTracking(curr, openBrackets + 1, closeBrackets)
                curr.pop()

        backTracking(["("], 1, 0)

        return self.ans
