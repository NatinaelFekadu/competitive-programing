class OrderedStream:

    def __init__(self, n: int):
        self.stream = n * [None]
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  
        self.stream[idKey] = value 
        if idKey > self.pointer:
            return []
        while self.pointer < len(self.stream) and self.stream[self.pointer]: 
            self.pointer += 1
        return self.stream[idKey:self.pointer]