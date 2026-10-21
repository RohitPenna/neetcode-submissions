from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(i):
            
            if i == n:
                return 1
            
            if i > n:
                return 0

            one = dfs(i + 1)
            two = dfs(i+2)

            return one + two
        
        return dfs(0)