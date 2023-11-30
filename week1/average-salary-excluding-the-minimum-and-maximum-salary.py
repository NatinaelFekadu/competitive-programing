class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = min(salary)
        maximum = max(salary)
        total = count = 0
        for val in salary:
            if val == minimum or val == maximum:
                continue
            else:
                total += val
                count += 1
        return total / count