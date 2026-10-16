from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, left):

            if  left == 0:
                return 1
            
            if i == len(coins) or left < 0:
                return 0
            
            stay = dfs(i, left-coins[i])
            move = dfs(i + 1, left)

            return stay + move
        
        return dfs(0, amount)
            