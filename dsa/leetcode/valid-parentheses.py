class Solution:
    def isValid(self, string: str) -> bool:
        parenthesis = {
            '(':')',
            '[':']',
            '{':'}'
        }
        my_stack = []
        for bracket in string:
            if bracket in parenthesis:
                my_stack.append(bracket)
            elif len(my_stack) > 0:
                curr = my_stack.pop()
                if parenthesis[curr] != bracket:
                    return False
            else:
                return False
        return len(my_stack) == 0