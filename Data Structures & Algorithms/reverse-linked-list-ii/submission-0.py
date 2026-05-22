# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        lp = dummy 
        c = head
        for i in range(left-1):
            lp, c = c, c.next

        prev = None
        for i in range(right-left+1):
            temp = c.next
            c.next = prev
            prev = c
            c = temp

        lp.next.next = c
        lp.next = prev
        return dummy.next
         

        