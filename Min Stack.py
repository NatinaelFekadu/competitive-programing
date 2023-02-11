class MinStack:

    def __init__(self):
        self.lst = []
        self.minimum = math.inf

    def push(self, x: int) -> None:
        self.lst.append(x)
        if x < self.minimum:
            self.minimum = x

    def pop(self) -> None:
        ret = self.lst.pop()
        if self.lst:
            self.minimum = min(self.lst)
        else:
            self.minimum = math.inf

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return self.minimum
