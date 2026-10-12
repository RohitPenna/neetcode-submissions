# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        queue.append([root])

        res = []

        if not root:
            return []

        while queue:
            x = queue.popleft()

            temp = []
            values = []

            for i in x:
                temp.append(i.val)
                if i.left:
                    values.append(i.left)
                if i.right:
                    values.append(i.right)
            
            res.append(temp)
            
            if values:
                queue.append(values)

        return res
