class MyQueue:

    def __init__(self):
        self.top = []

    def push(self, x: int) -> None:
        return self.top.append(x)
        

    def pop(self) -> int:
        first = self.top[0]
        self.top = self.top[1:]
        return first
        

    def peek(self) -> int:
        return self.top[0]

    def empty(self) -> bool:
        return self.top == []
