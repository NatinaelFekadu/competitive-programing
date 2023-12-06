class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        total = (weeks * (7*weeks + 49)) // 2
        remaining = n % 7
        remaining_sum = remaining *(2 * (weeks + 1) + (remaining - 1))//2
        return total + remaining_sum