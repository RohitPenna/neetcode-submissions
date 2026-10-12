# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        ids = {}
        next_id = 1
        seen = set()

        def dfs(node, track):
            nonlocal next_id

            if node is None:
                return 0

            left = dfs(node.left, track)
            right = dfs(node.right, track)

            key = (node.val, left, right)

            if key not in ids:
                ids[key] = next_id
                next_id += 1

            subtree_id = ids[key]

            if track:
                seen.add(subtree_id)

            return subtree_id

        dfs(root, True)
        target = dfs(subRoot, False)

        return target in seen