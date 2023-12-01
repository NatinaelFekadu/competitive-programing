class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            new_string += word1[i]
            new_string += word2[j]
            i,j = i + 1, j + 1
        new_string += word1[i:]
        new_string += word2[j:]
        return new_string