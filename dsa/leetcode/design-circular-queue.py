class ListNode:
    def __init__(self, val = None, next_node = None):
        self.val = val
        self.next = next_node

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.head = None
        self.tail = None
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if self.cnt == self.cap:
            return False
        
        if self.cnt == 0:
            self.head = ListNode(value)
            self.tail = self.head
        
        elif self.cnt != 0:
            to_add = ListNode(value)
            self.tail.next = to_add
            self.tail = to_add
        
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.cnt == 0:
            return False
        
        self.head = self.head.next
        self.cnt -= 1
        return True


    def Front(self) -> int:
        if self.cnt == 0:
            return -1     
        return self.head.val

    def Rear(self) -> int:
        if self.cnt == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()