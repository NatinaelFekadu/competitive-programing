# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = ListNode()
        curr.next = head
        prev = curr
        for _ in range(left-1):
            prev = prev.next
        present = prev.next
        print(prev)
        for _ in range(right - left):
            then = present.next
            present.next = then.next
            then.next = prev.next
            prev.next = then
        return curr.next


        