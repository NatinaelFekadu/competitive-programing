class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0 for _ in range(k)]
        self.length = 0
        self.max_size = k
        self.beg = self.end = 0
        

    def insertFront(self, value: int) -> bool:
        
        if self.length == self.max_size:
            return False
        
        self.length += 1
        
        self.beg = (self.beg - 1) % self.max_size
        self.arr[self.beg] = value
              
        
        return True
        

    def insertLast(self, value: int) -> bool:
        
        if self.length == self.max_size:
            return False
        
        self.length += 1
        
        self.arr[self.end] = value
        self.end = (self.end + 1) % self.max_size
        
        return True
        

    def deleteFront(self) -> bool:
        
        if self.length == 0:
            return False
        
        self.length -= 1
        self.beg = (self.beg + 1) % self.max_size
        
        return True
        

    def deleteLast(self) -> bool:
                
        if self.length == 0:
            return False
        
        self.length -= 1
        self.end = (self.end - 1) % self.max_size
        
        return True
        

    def getFront(self) -> int:
        
        if self.length == 0:
            return -1
        
        return self.arr[self.beg]
        

    def getRear(self) -> int:
        
        if self.length == 0:
            return -1
        
        return self.arr[self.end-1]
        

    def isEmpty(self) -> bool:
        
        return self.length == 0
        

    def isFull(self) -> bool:
        
        return self.length == self.max_size
