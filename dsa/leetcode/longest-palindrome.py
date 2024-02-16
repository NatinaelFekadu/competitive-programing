class Solution:
    def longestPalindrome(self,s:str) -> int:
        unique = set()
        for char in s:
            if char not in unique:
                unique.add(char)
            else:
                unique.remove(char)
        if len(unique) != 0:
            return len(s) - len(unique) + 1
        else:
            return len(s)