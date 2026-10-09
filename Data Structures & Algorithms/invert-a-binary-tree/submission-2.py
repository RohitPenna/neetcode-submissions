# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if root is None:
                return
            
            x = root.left
            root.left = root.right
            root.right = x

            dfs(root.left)
            dfs(root.right)

        x = root
        dfs(root)
        return x