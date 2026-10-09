from collections import deque

#CHECK BOTH SOLUTUONS SUBMITTED

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if p is None and q is None:
                continue

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True