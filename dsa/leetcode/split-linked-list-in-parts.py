# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        res = [ListNode() for _ in range(k)]
        if count <= k:
            curr = head
            for i in range(count):
                res[i].val = curr.val
                curr = curr.next
            for i in range(count, k):
                res[i] = None
            
        else:
            curr = head
            div = count // k
            rem = count % k
            for i in range(k):
                temp = curr
                j = 1
                res[i].val = curr.val
                while j < div:
                    res[i].next = curr.next
                    temp = temp.next
                    j += 1
                if rem > 0:
                    res[i].next = curr.next
                    temp = temp.next
                    rem -= 1
                curr = temp.next
                temp.next = None

        return res
        
        