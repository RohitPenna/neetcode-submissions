from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):

                if r == 0 and c == 0:
                    continue
                
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        
        return dp[-1][-1]
        
        
        '''
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if i == m or j == n:
                return 0
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)

            return down + right
        
        return dfs(0, 0)
        '''