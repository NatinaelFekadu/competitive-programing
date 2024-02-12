# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise, rabbit = head, head
        while True:
            if not rabbit or not rabbit.next or not rabbit.next.next:
                return None
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == tortoise:
                break
        tortoise = head
        while tortoise != rabbit:
            tortoise = tortoise.next
            rabbit = rabbit.next
        return tortoise