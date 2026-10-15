from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(remaining):

            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(remaining - coin))

            return ans

        result = dfs(amount)

        return result if result != float('inf') else -1


