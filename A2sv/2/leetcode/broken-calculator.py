class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        min_ope = 0
        while target > startValue:
            if target % 2 != 0:
                target += 1
                min_ope += 1
            target //= 2
            min_ope += 1
        min_ope += startValue - target
        return min_ope