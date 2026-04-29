# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy =ListNode(0, head)
        l, r = dummy, head

        # move right pointer to n + 1
        while n > 0 and r:
            r = r.next
            n -= 1

        # find the (n - 1)th node
        while r:
            l = l.next
            r = r.next

        # delete the nth node
        l.next = l.next.next 

        return dummy.next

        