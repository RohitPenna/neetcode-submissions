class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None

        def dfs(node):
            nonlocal count, ans

            if not node or ans is not None:
                return

            dfs(node.left)

            if ans is not None:
                return

            count += 1

            if count == k:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans