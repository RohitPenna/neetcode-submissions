# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def dfs (node, minx, maxx):

            if not node:
                return True
            
            if node.val <= minx or node.val >= maxx:
                return False
            
            return dfs(node.left, minx, node.val) and dfs(node.right, node.val, maxx)
        
        x = dfs(root, float('-inf'), float('inf'))

        return x

