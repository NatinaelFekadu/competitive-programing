class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        list_index = float("inf")
        for i,word1 in enumerate(list1):
            for j,word2 in enumerate(list2):
                if word1 == word2:
                    if (j + i < list_index and not result) or (j + i == list_index):
                        result.append(word1)
                        list_index = j + i
                    elif j + i < list_index and result:
                        result.pop()
                        result.append(word1)
                        list_index = j + i
        return result