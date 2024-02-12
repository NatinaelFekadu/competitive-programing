# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, rabbit = head, head
        while True:
            if not rabbit or not rabbit.next or not rabbit.next.next:
                return False
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == tortoise:
                return True
        