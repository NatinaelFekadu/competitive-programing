class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            rem = n % 3
            n = n // 3
            if rem != 1 and rem != 0:
                return False
        return True