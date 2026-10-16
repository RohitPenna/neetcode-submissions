from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(r, c):

            longest = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):

                    longest = max(
                        longest,
                        1 + dfs(nr, nc)
                    )

            return longest

        ans = 0

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans