# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root == None:
            return res
        
        q = collections.deque()
        q.append(root)

        while q:
            qlength = len(q)
            level = []
            for i in range(qlength):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left: 
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)
        
        return res