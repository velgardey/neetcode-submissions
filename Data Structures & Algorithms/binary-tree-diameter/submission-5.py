# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def dfs(root):
            nonlocal dia

            if root == None:
                return 0
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            dia = max(dia, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)

        dfs(root)
        return dia
