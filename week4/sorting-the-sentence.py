class Solution:
    def sortSentence(self, s: str) -> str:
        sentence_array = list(s.split())
        sorted_sentence = len(sentence_array) * [' ']
        for i in range(len(sentence_array)):
            word = sentence_array[i]
            index = int(word[-1])
            sorted_sentence[index-1] = word[:len(word)-1]
        original_sentence = (" ".join(map(str,sorted_sentence))) 
        return original_sentence
