class Solution:
    #01001110
    def minimumSteps(self, s: str) -> int:
        placed, steps = 0, 0
        for i, val in enumerate(s):
            if val == "0":
                steps += (i - placed)
                placed += 1
        return steps