class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        res = ""
        replaced = False
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        print(palindrome[:-1])
        return palindrome[:-1] + "b"