class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        hashmap = {}
        for i,row in enumerate(rows):
            for j in range(len(row)):
                hashmap[row[j]] = i
        def is_in_the_same_row(word:str) -> bool:
            row = hashmap[word[0].lower()]
            for char in word:
                if hashmap[char.lower()] != row:
                    return False
            return True
        for word in words:
            if is_in_the_same_row(word) == True:
                result.append(word)
        return result