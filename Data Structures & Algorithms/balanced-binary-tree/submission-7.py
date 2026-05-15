# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root == None:
                return [True, 0] # [isBalanced, height]

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            balanced = leftHeight[0] and rightHeight[0] and abs(leftHeight[1] - rightHeight[1]) <= 1
            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]

        return dfs(root)[0]