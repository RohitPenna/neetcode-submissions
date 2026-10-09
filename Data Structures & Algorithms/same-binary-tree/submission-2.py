# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = deque()

        if q is None and p is None:
            return True
        
        if q is None or p is None:
            return False

        queue.append(p)
        queue.append(q)

        while queue:

            vp = queue.popleft()
            vq = queue.popleft()

            if vp.val != vq.val:
                return False
            
            if vp.left and vq.left:
                queue.append(vp.left)
                queue.append(vq.left)
            elif vp.left or vq.left:
                return False

            if vp.right and vq.right:
                queue.append(vp.right)
                queue.append(vq.right)
            elif vp.right or vq.right:
                return False
        
        return True
        