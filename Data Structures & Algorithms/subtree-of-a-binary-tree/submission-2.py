# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True

        if root is None:
            return False

        def isSameTree(p, q):
            queue = deque([(p, q)])

            while queue:
                x, y = queue.popleft()

                if x is None and y is None:
                    continue

                if x is None or y is None:
                    return False

                if x.val != y.val:
                    return False

                queue.append((x.left, y.left))
                queue.append((x.right, y.right))

            return True

        def find(node):
            if node is None:
                return False

            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True

            return find(node.left) or find(node.right)

        return find(root)