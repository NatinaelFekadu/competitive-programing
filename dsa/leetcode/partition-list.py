# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than = ListNode()
        greater_or_equal = ListNode()

        before = less_than
        after = greater_or_equal

        current = head
        while current:
            if current.val < x:
               before.next = current
               before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        print(after)
        print(greater_or_equal)
        before.next = greater_or_equal.next
        after.next = None
        return less_than.next
        