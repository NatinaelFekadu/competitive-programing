# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        for _ in range(n):
            right = right.next

        if not right:
            return head.next

        left = head
        while right.next:
            right = right.next
            left = left.next
        temp = left.next
        left.next = temp.next
        return head
        
        
        