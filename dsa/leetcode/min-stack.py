class MinStack:

    def __init__(self):
        self.min_stack = []
        self.minimum = []

    def push(self, x: int) -> None:
        if len(self.min_stack) > 0:
            self.minimum.append(min(x,self.minimum[-1]))
        else:
            self.minimum.append(x)
        self.min_stack.append(x)
            
    
    def pop(self) -> None:
        self.min_stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()