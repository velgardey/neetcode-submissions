# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower, upper = float("-inf"), float("inf")

        def dfs(root, lower, upper):
            if root == None:
                return True
            if root.val > lower and root.val < upper:
                return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper) 
            else:
                return False

        
        return dfs(root, lower, upper)
