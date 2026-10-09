# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        balanced = True
        
        def dfs(node):

            nonlocal balanced

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            balanced = balanced and abs(left - right) <= 1

            return 1 + max(dfs(node.left), dfs(node.right))

        dfs(root)
        return balanced
        