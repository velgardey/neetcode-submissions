# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # find the mid point of the linked list to divide the ll into two halves
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        secondhalf = slow.next # starting point for the next half of the LL

        # Now we reverse the links of the second half
        prev = slow.next = None 
        while secondhalf :
            temp = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = temp

        # Now we merge the two LL together
        firsthalf, secondhalf = head, prev
        while secondhalf and firsthalf:
            temp1, temp2 = firsthalf.next, secondhalf.next
            firsthalf.next = secondhalf
            secondhalf.next = temp1
            firsthalf, secondhalf = temp1, temp2
            


        