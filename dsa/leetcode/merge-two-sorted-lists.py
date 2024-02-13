# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        l3=None
        while list1:
            if list1 is not None:
                arr.append(list1.val)
                list1=list1.next
            
        while list2:
            if list2 is not None:
                arr.append(list2.val)
                list2=list2.next
              
        arr.sort(reverse=True)  
        for i in arr:
            l3=ListNode(i,l3)
        return l3







        