# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # seen = set()
        # while headA or headB:
        #     if headA and headA in seen:
        #         return headA
        #     seen.add(headA)
        #     if headA:
        #       headA=headA.next
        #     if headB and headB in seen:
        #         return headB
        #     seen.add(headB)
        #     if headB:
        #         headB = headB.next
        curr1, curr2 = headA, headB
        size1, size2 = 0, 0
        while curr1 and curr1.next:
            curr1 = curr1.next
            size1 += 1
        while curr2 and curr2.next:
            curr2 = curr2.next
            size2 += 1
        current1, current2 = headA, headB
        if size1 > size2:
            for _ in range(size1 - size2):
                current1 = current1.next
        else:
            for _ in range(size2 - size1):
                current2 = current2.next
        while current1 != current2:
            current1 = current1.next
            current2 = current2.next
        return current1
