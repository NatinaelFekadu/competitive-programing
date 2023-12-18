class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, right = 0, min(k, len(s))

        while left < len(s):
            s = s[:left] + s[left:right][::-1] + s[right:]
            
            left += 2 * k
            right = min(left + k, len(s))

        return s