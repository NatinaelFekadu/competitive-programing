class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        unique = set(s)
        for i in range(len(s)):
            if s[i].upper() not in unique or s[i].lower() not in unique:
                first = self.longestNiceSubstring(s[:i])
                second = self.longestNiceSubstring(s[i + 1 :])
                if len(first) >= len(second):
                    return first
                return second
        return s
