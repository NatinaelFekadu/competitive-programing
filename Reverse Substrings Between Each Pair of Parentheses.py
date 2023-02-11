class Solution:
    def reverseParentheses(self, s: str) -> str:
        indexStack = []
        stringList = list(s)
        for i, char in enumerate(stringList):
            if char == '(':
                indexStack.append(i)
            if char == ')':
                startIndex = indexStack.pop()
                section = stringList[startIndex:i+1]
                section.reverse()
                stringList[startIndex:i+1] = section
        return ''.join(list(filter(lambda char: char != '(' and char != ')', stringList))) 
