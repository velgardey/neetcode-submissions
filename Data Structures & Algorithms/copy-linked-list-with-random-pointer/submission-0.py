"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = { None : None } # Edge case to allow for null nexts and randoms

        # first pass to store only the node copies
        cur = head
        while cur:
            copy = Node(cur.val)
            copyMap[cur] = copy
            cur = cur.next

        # second pass to make the pointer connections in the copied nodes
        cur = head
        while cur:
            copy = copyMap[cur]
            copy.next = copyMap[cur.next]
            copy.random = copyMap[cur.random]
            cur = cur.next
        return copyMap[head]