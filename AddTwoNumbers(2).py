# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        trav=ListNode(0)
        curr = trav
        remainder  = 0

        while l1 or l2 or remainder:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            sum = x1 + x2 + remainder
            remainder = sum // 10

            curr.next = ListNode(sum%10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return trav.next
