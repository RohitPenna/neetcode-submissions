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

            for i in x:
                temp.append(i.val)
            
            res.append(temp)

            temp = []
            
            for i in x:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            if temp:
                queue.append(temp)

        return res
