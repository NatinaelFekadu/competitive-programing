class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_string = ""
        j = 0
        for i,val in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                new_string += " "
                j += 1
            new_string += val
        return new_string
