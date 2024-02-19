class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        operations = ['+','-','*','/']
        for item in tokens:
            if item not in operations:
                item = int(item)
                my_stack.append(item)
            else:
                first = my_stack.pop()
                second = my_stack.pop()
                if item == '+':
                    my_stack.append(second + first)
                elif item == '-':
                    my_stack.append(second - first)
                elif item == '*':
                    my_stack.append(second * first)
                else:
                    if second // first >= 0:
                        my_stack.append(second // first)
                    else:
                        my_stack.append(ceil(second/first))
        return my_stack.pop()