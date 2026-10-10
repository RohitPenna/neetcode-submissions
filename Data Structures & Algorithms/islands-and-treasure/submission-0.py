from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()

            for r, c in [(row+1, col), (row-1, col),
                         (row, col+1), (row, col-1)]:

                if (r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    grid[r][c] != 2147483647):
                    continue

                grid[r][c] = grid[row][col] + 1
                queue.append((r, c))