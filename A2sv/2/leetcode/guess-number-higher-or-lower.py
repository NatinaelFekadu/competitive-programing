# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(0) == 0:
            return 0
        if guess(n) == 0:
            return n
        def rec(i = 0, n = n):
            start, end = i, n
            if guess((start + end) // 2) == 0:
                return (start + end) // 2
            elif guess((start + end) // 2) == 1:
                return rec((start + end) // 2, end)
            else:
                return rec(start, (start + end) // 2)
        def rec2(i = 0, n = n):
            start, end = i, n
            if guess((start + end) // 2) == 0:
                return (start + end) // 2
            elif guess((start + end) // 2) == 1:
                return rec2((start + end) // 2 + 1, end)
            else:
                return rec2(start, (start + end) // 2 + 1)
        return rec() if n % 2 == 0 else rec2()