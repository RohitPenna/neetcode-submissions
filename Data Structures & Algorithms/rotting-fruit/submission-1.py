from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        count = 0
        fc = 0
        while queue:
            temp = []
            while queue:
                row, col = queue.popleft()
                for r, c in [[row+1, col], [row-1, col], [row, col-1], [row,col+1]]:
                    
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                        continue
                    
                    grid[r][c] = 2
                    fc += 1
                    temp.append((r, c))

            for i in temp:
                queue.append(i)
            if queue: count += 1
        
        return count if fc == fresh else -1
         