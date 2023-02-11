class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            try:     stack.append(float(s))
            except:  stack.append( int( eval(str(float(stack.pop(-2))) + s + str(stack.pop(-1)) ) ))
        return int(stack.pop())
