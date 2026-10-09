# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def dfs(root, curDepth):
            if root is None:
                return curDepth - 1
            
            return max(dfs(root.left, curDepth + 1), dfs(root.right, curDepth + 1))

        x = dfs(root, 1)
        return x    