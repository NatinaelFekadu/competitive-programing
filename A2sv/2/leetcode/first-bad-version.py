# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        firstBad = 0
        while l <= r:
            m = (l + r) // 2
            isBad = isBadVersion(m)
            if not isBad:
                l = m + 1
            else:
                r = m - 1
                firstBad = m
        return firstBad