class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited):
                return

            visited.add((r, c))

            for row, col in [(r+1, c), (r-1, c),
                             (r, c+1), (r, c-1)]:

                if (row < 0 or row >= rows or
                    col < 0 or col >= cols):
                    continue

                if heights[row][col] >= heights[r][c]:
                    dfs(row, col, visited)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)

        ans = []

        for r, c in pacific:
            if (r, c) in atlantic:
                ans.append([r, c])

        return ans