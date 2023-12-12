class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.split())[::-1]
        return " ".join(s)
        