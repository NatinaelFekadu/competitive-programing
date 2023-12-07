class Solution:
    def largestOddNumber(self, num: str) -> str:
        right = len(num) - 1
        odd_found = False
        while right >= 0:
            if int(num[right]) % 2 != 0:
                odd_found = True
                break
            else:
                right -= 1
        return num[:right+1] if odd_found else ""