class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        max_vowels = 0
        left, right = 0, k

        for val in s[:right]:
            if val in vowels:
                max_vowels += 1
        count_vowels = max_vowels
        while right < len(s):
            if s[left] in vowels:
                count_vowels -=1
            if s[right] in vowels:
                count_vowels += 1
            left, right = left + 1, right + 1
            max_vowels = max(max_vowels,count_vowels)
        return max_vowels
