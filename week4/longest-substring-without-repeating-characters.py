class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = max_len = 0
        for right, char in enumerate(s):
            while char in window:
                window.remove(s[left])
                left += 1
            max_len = max(max_len,right - left + 1)
            window.add(char)
        return max_len