class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_one = word_two = ""
        for string in word1:
            word_one += string
        for string in word2:
            word_two += string
        return word_one == word_two