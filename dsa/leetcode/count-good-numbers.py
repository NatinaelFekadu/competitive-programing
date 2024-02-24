class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        good, x, i = 5 ** (n % 2), 4 * 5, n // 2
        while i > 0:
            if i % 2 == 1:
                good = good * x % mod
            x = x * x % mod
            i //= 2
        return good