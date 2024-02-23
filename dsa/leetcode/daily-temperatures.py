class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current = temperatures[i]
            index = i
            while stack and current > stack[-1][0]:
                val, prev = stack.pop()
                curr = index - prev
                res[prev] = curr
            stack.append([current, index])
        return res