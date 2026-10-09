# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque()

        if not root:
            return []

        queue.append([root])

        res = []
        
        while queue:
            x = queue.popleft()
            res.append(x[-1].val)

            temp = []
            
            for i in x:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            if temp:
                queue.append(temp)
        
        return res





        