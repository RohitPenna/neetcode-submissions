from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dfs(i, j):
            if i == m or j == n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            down = dfs(i + 1, j)
            right = dfs(i, j + 1)

            return down + right

        return dfs(0, 0)